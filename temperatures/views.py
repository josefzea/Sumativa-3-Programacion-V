from rest_framework import viewsets, permissions
from .models import CityTemperature
from .serializers import CityTemperatureSerializer

class CityTemperatureViewSet(viewsets.ModelViewSet):
    queryset = CityTemperature.objects.all().order_by('-last_updated')
    serializer_class = CityTemperatureSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
