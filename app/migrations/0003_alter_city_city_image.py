# Generated by Django 3.2.5 on 2021-07-15 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_city_city_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='city_image',
            field=models.ImageField(blank=True, null=True, upload_to='tutorial/site/public/static'),
        ),
    ]
