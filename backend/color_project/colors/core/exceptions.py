class ColorSpaceError(Exception):
    """Base exception for color space related errors"""
    pass

class ColorValidationError(ColorSpaceError):
    """Exception raised when color values are invalid"""
    pass

class ColorSpaceRegistrationError(ColorSpaceError):
    """Exception raised when there's an error registering a color space"""
    pass

class ColorConversionError(ColorSpaceError):
    """Exception raised when color conversion fails"""
    pass

# Example usage:
"""
try:
    if not 0 <= value <= 255:
        raise ColorValidationError("RGB values must be between 0 and 255")
except ColorValidationError as e:
    # Handle validation error
    pass
"""