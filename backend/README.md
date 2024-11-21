## Backend (Django)

### Project Setup

```bash
pipenv shell
pipenv install django djangorestframework django-cors-headers
django-admin startproject color_project
cd color_project
python manage.py startapp colors
```

### Project Structure

```
color_project/
├── colors/
│   ├── core/
│   │   ├── base.py         # Base color space classes
│   │   └── exceptions.py   # Custom exceptions
│   ├── implementations/
│   │   ├── rgb.py         # RGB color space
│   │   └── hsl.py         # HSL color space
│   ├── services/
│   │   └── color_service.py # Business logic
│   ├── api/
│   │   ├── urls.py        # API routing
│   │   └── views.py       # API endpoints
│   └── tests/
│       ├── test_color_spaces.py
│       └── test_api.py
└── manage.py
```

### Implementation Steps

1. **Core Components**

   - Create abstract base ColorSpace class
   - Implement validation methods
   - Define required interfaces

2. **Color Space Implementations**

   - RGB: Standard RGB color space (0-255)
   - HSL: Hue (0-360), Saturation/Lightness (0-100)
   - BRGB: Extended RGB (0-10000)

3. **Service Layer**

   - Color space registry
   - Random swatch generation
   - Color space management

4. **API Layer**
   - Endpoint: GET /api/swatches/
   - Query params: count (default=5)
   - Error handling
   - CORS configuration

### Extension Guide

To add new color spaces:

1. Create new class inheriting from ColorSpace
2. Implement required methods:
   - to_rgb()
   - to_dict()
   - generate_random()
3. Register with ColorService
4. Update frontend color conversion logic

Example for BRGB:

```python
@dataclass
class BRGBColor(ColorSpace):
    red: int    # 0-10000
    green: int  # 0-10000
    blue: int   # 0-10000

    def to_rgb(self) -> Tuple[int, int, int]:
        return (
            int(self.red * 255 / 10000),
            int(self.green * 255 / 10000),
            int(self.blue * 255 / 10000)
        )
```
