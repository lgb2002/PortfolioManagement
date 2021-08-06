# Generated by Django 2.0.13 on 2021-08-06 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0028_auto_20210806_1831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='image',
            field=models.FileField(default='fruit.jpg', upload_to=''),
        ),
        migrations.AlterField(
            model_name='introduce',
            name='image1',
            field=models.FileField(default='orange.svg', upload_to=''),
        ),
        migrations.AlterField(
            model_name='introduce',
            name='image2',
            field=models.FileField(default='orange.svg', upload_to=''),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='video_contents',
            field=models.FileField(default='test.mp4', upload_to=''),
        ),
    ]
