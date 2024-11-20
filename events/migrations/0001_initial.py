# Generated by Django 4.2.16 on 2024-11-20 18:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BandName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ensemble',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slots', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('venue_name', models.CharField(max_length=255)),
                ('postcode', models.CharField(blank=True, max_length=20, null=True)),
                ('arrival_time', models.TimeField(blank=True, null=True)),
                ('start_time', models.TimeField(blank=True, null=True)),
                ('finish_time', models.TimeField(blank=True, null=True)),
                ('requests', models.TextField(blank=True, null=True)),
                ('band_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='events.bandname')),
                ('ensemble', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='events.ensemble')),
            ],
        ),
        migrations.CreateModel(
            name='Slot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='slots', to='events.event')),
                ('musician', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='slots', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
