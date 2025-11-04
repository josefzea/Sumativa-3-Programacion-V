from django.db import models

class Temperature(models.Model):
    city = models.CharField(max_length=100)
    temperature = models.FloatField()
    date_recorded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.city} - {self.temperature}°C ({self.date_recorded.date()})"


class CityTemperature(models.Model):
    city = models.CharField(max_length=100, unique=True)
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.city}: {self.temperature}°C (actualizado {self.last_updated.strftime('%Y-%m-%d %H:%M')})"
