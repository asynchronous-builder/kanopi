import unittest
from colors.core.exceptions import ColorSpaceError, ColorValidationError
from colors.implementations.rgb import RGBColor
from colors.implementations.hsl import HSLColor
from colors.services.color_service import ColorService


class TestRGBColor(unittest.TestCase):
    def test_valid_rgb(self):
        color = RGBColor(red=255, green=128, blue=0)
        self.assertEqual(color.to_rgb(), (255, 128, 0))
        
    def test_invalid_rgb(self):
        with self.assertRaises(ColorValidationError):
            RGBColor(red=256, green=0, blue=0).validate()
            
    def test_random_generation(self):
        color = RGBColor.generate_random()
        self.assertTrue(0 <= color.red <= 255)
        self.assertTrue(0 <= color.green <= 255)
        self.assertTrue(0 <= color.blue <= 255)


class TestHSLColor(unittest.TestCase):
    def test_valid_hsl(self):
        color = HSLColor(hue=180, saturation=50, lightness=50)
        rgb = color.to_rgb()
        self.assertTrue(all(isinstance(v, int) for v in rgb))
        self.assertTrue(all(0 <= v <= 255 for v in rgb))
        
    def test_invalid_hsl(self):
        with self.assertRaises(ColorValidationError):
            HSLColor(hue=361, saturation=50, lightness=50).validate()
            
    def test_hsl_to_rgb_conversion(self):
        # Test known HSL to RGB conversions
        test_cases = [
            (HSLColor(0, 0, 0), (0, 0, 0)),  # Black
            (HSLColor(0, 0, 100), (255, 255, 255)),  # White
            (HSLColor(0, 100, 50), (255, 0, 0)),  # Red
        ]
        for hsl, expected_rgb in test_cases:
            self.assertEqual(hsl.to_rgb(), expected_rgb)


class TestColorService(unittest.TestCase):
    def setUp(self):
        self.service = ColorService()
        self.service.register_color_space(RGBColor)
        self.service.register_color_space(HSLColor)
        
    def test_swatch_generation(self):
        swatches = self.service.generate_swatches(count=5)
        self.assertEqual(len(swatches), 5)
        for swatch in swatches:
            self.assertIn('type', swatch)
            self.assertIn(swatch['type'], ['rgb', 'hsl'])
            
    def test_duplicate_registration(self):
        with self.assertRaises(ColorSpaceError):
            self.service.register_color_space(RGBColor)
            
    def test_invalid_count(self):
        with self.assertRaises(ValueError):
            self.service.generate_swatches(count=0)
