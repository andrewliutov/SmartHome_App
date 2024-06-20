from django.db import migrations, models
import django.db.models.deletion
import measurement.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Датчик')),
                ('description', models.TextField(max_length=300, verbose_name='Описание')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Measurement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.DecimalField(decimal_places=1, max_digits=4, verbose_name='Температура')),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='Дата')),
                ('image', models.ImageField(blank=True, null=True, upload_to=measurement.models.image_path)),
                ('sensor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='measurements', to='measurement.sensor')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
