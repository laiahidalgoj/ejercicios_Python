# Generated by Django 4.1.3 on 2022-11-10 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_image_film_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.FileField(upload_to='films/'),
        ),
    ]
