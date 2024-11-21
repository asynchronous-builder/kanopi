# colors/implementations/rgb.py
import random
from dataclasses import dataclass
from colors.core.base import ColorSpace
from colors.core.exceptions import ColorValidationError
from typing import Tuple, Dict, Any

@dataclass
class RGBColor(ColorSpace):
    red: int
    green: int
    blue: int
    
    def validate(self) -> None:
        for value in [self.red, self.green, self.blue]:
            if not 0 <= value <= 255:
                raise ColorValidationError(f"RGB values must be between 0 and 255, got {value}")
    
    def to_rgb(self) -> Tuple[int, int, int]:
        self.validate()
        return (self.red, self.green, self.blue)
    
    def to_dict(self) -> Dict[str, Any]:
        self.validate()
        return {
            "type": "rgb",
            "red": self.red,
            "green": self.green,
            "blue": self.blue
        }
    
    @classmethod
    def generate_random(cls) -> 'RGBColor':
        return cls(
            red=random.randint(0, 255),
            green=random.randint(0, 255),
            blue=random.randint(0, 255)
        )