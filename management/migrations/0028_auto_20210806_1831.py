# Generated by Django 2.0.13 on 2021-08-06 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0027_auto_20210806_1736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='image',
            field=models.FileField(default='image/fruit.jpg', upload_to=''),
        ),
        migrations.AlterField(
            model_name='introduce',
            name='image1',
            field=models.FileField(default='image/orange.svg', upload_to=''),
        ),
        migrations.AlterField(
            model_name='introduce',
            name='image2',
            field=models.FileField(default='image/orange.svg', upload_to=''),
        ),
    ]