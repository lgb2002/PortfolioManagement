# Generated by Django 2.0.13 on 2021-08-06 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0024_auto_20210806_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='video_contents',
            field=models.FileField(default='media/video/test.mp4', upload_to=''),
        ),
    ]
