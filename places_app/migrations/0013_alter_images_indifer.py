# Generated by Django 4.2.5 on 2023-10-26 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places_app', '0012_alter_images_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='indifer',
            field=models.CharField(choices=[['1', '1'], ['2', '2']], max_length=1),
        ),
    ]
