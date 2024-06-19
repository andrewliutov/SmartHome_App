from django.db import models


def image_path(instance, filename):
    return '/'.join([
        'sensors_images',
        f'sensor_id_{instance.sensor.id}',
        filename,
    ])


class Sensor(models.Model):
    name = models.CharField(max_length=50, verbose_name='Датчик')
    description = models.TextField(max_length=300, verbose_name='Описание')

    class Meta:
        ordering = ['-id']


class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
    temperature = models.DecimalField(max_digits=4, decimal_places=1, verbose_name='Температура')
    created_at = models.DateTimeField(auto_now=True, verbose_name='Дата')
    image = models.ImageField(upload_to=image_path, null=True, blank=True)

    class Meta:
        ordering = ['-created_at']
