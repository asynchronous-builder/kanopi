# colors/api/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from colors.services.color_service import ColorService
from colors.core.exceptions import ColorSpaceError, ColorValidationError
from colors.implementations.rgb import RGBColor
from colors.implementations.hsl import HSLColor
from django.conf import settings

class SwatchesView(APIView):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.color_service = ColorService()
        
        # Register default color spaces
        self.color_service.register_color_space(RGBColor)
        self.color_service.register_color_space(HSLColor)
        
        # Register additional color spaces from settings
        for color_space in getattr(settings, 'ADDITIONAL_COLOR_SPACES', []):
            self.color_service.register_color_space(color_space)
    
    def get(self, request: Request) -> Response:
        try:
            count = int(request.query_params.get('count', 5))
            if count > settings.MAX_SWATCH_COUNT:
                return Response(
                    {"error": f"Maximum swatch count is {settings.MAX_SWATCH_COUNT}"},
                    status=status.HTTP_400_BAD_REQUEST
                )
                
            swatches = self.color_service.generate_swatches(count)
            return Response(swatches)
            
        except (ColorSpaceError, ColorValidationError) as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        except ValueError as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )