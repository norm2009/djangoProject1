# Generated by Django 4.2.5 on 2023-10-26 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places_app', '0002_images_remove_place_text_place_description_long_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='images',
            name='place',
            field=models.CharField(default=0, max_length=200, verbose_name='Place'),
            preserve_default=False,
        ),
    ]
