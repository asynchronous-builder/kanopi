# colors/core/base.py
from abc import ABC, abstractmethod
from typing import Tuple, Dict, Any, Protocol
from dataclasses import dataclass

class ColorSpaceProtocol(Protocol):
    def to_rgb(self) -> Tuple[int, int, int]: ...
    def to_dict(self) -> Dict[str, Any]: ...
    @classmethod
    def generate_random(cls) -> 'ColorSpaceProtocol': ...

@dataclass
class ColorSpace(ABC):
    """Base class for all color spaces"""
    
    @abstractmethod
    def to_rgb(self) -> Tuple[int, int, int]:
        """Convert color to RGB format"""
        pass
    
    @abstractmethod
    def to_dict(self) -> Dict[str, Any]:
        """Convert color to dictionary for serialization"""
        pass
    
    @classmethod
    @abstractmethod
    def generate_random(cls) -> 'ColorSpace':
        """Generate random color in this color space"""
        pass
    
    def validate(self) -> None:
        """Validate color values"""
        pass