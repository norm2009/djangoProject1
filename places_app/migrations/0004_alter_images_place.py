# Generated by Django 4.2.5 on 2023-10-26 18:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('places_app', '0003_images_place'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='place',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='places_app.place'),
        ),
    ]
