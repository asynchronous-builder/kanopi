# colors/services/color_service.py
from typing import List, Type, Dict, Any
from colors.core.base import ColorSpace
from colors.core.exceptions import ColorSpaceError
import random

class ColorService:
    def __init__(self):
        self._color_spaces: List[Type[ColorSpace]] = []
        self._space_registry: Dict[str, Type[ColorSpace]] = {}
    
    def register_color_space(self, color_space: Type[ColorSpace]) -> None:
        """Register a new color space implementation"""
        if not issubclass(color_space, ColorSpace):
            raise ColorSpaceError("Color space must inherit from ColorSpace")
            
        space_type = color_space.generate_random().to_dict()["type"]
        if space_type in self._space_registry:
            raise ColorSpaceError(f"Color space type '{space_type}' already registered")
            
        self._color_spaces.append(color_space)
        self._space_registry[space_type] = color_space
    
    def get_color_space(self, space_type: str) -> Type[ColorSpace]:
        """Get color space implementation by type"""
        if space_type not in self._space_registry:
            raise ColorSpaceError(f"Unknown color space type: {space_type}")
        return self._space_registry[space_type]
    
    def generate_swatches(self, count: int = 5) -> List[Dict[str, Any]]:
        """Generate random color swatches"""
        if not self._color_spaces:
            raise ColorSpaceError("No color spaces registered")
            
        if count < 1:
            raise ValueError("Count must be positive")
            
        return [
            random.choice(self._color_spaces).generate_random().to_dict()
            for _ in range(count)
        ]