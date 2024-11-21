# colors/implementations/hsl.py
import random
from dataclasses import dataclass
from colors.core.base import ColorSpace
from colors.core.exceptions import ColorValidationError
from typing import Tuple, Dict, Any


@dataclass
class HSLColor(ColorSpace):
    hue: int
    saturation: int
    lightness: int
    
    def validate(self) -> None:
        if not 0 <= self.hue <= 360:
            raise ColorValidationError(f"Hue must be between 0 and 360, got {self.hue}")
        if not 0 <= self.saturation <= 100:
            raise ColorValidationError(f"Saturation must be between 0 and 100, got {self.saturation}")
        if not 0 <= self.lightness <= 100:
            raise ColorValidationError(f"Lightness must be between 0 and 100, got {self.lightness}")

    def to_rgb(self) -> Tuple[int, int, int]:
        self.validate()
        h, s, l = self.hue / 360, self.saturation / 100, self.lightness / 100
        
        if s == 0:
            rgb = l, l, l
        else:
            def hue_to_rgb(p: float, q: float, t: float) -> float:
                if t < 0: t += 1
                if t > 1: t -= 1
                if t < 1/6: return p + (q - p) * 6 * t
                if t < 1/2: return q
                if t < 2/3: return p + (q - p) * (2/3 - t) * 6
                return p

            q = l * (1 + s) if l < 0.5 else l + s - l * s
            p = 2 * l - q
            
            rgb = (
                hue_to_rgb(p, q, h + 1/3),
                hue_to_rgb(p, q, h),
                hue_to_rgb(p, q, h - 1/3)
            )
            
        return tuple(int(x * 255) for x in rgb)
    
    def to_dict(self) -> Dict[str, Any]:
        self.validate()
        return {
            "type": "hsl",
            "hue": self.hue,
            "saturation": self.saturation,
            "lightness": self.lightness
        }
    
    @classmethod
    def generate_random(cls) -> 'HSLColor':
        return cls(
            hue=random.randint(0, 360),
            saturation=random.randint(0, 100),
            lightness=random.randint(0, 100)
        )