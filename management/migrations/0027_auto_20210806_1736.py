# Generated by Django 2.0.13 on 2021-08-06 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0026_auto_20210806_1613'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='email',
            field=models.CharField(default='xxx@xxx.xxx', max_length=100),
        ),
        migrations.AddField(
            model_name='request',
            name='phone_number',
            field=models.CharField(default='XXX-XXXX-XXXX', max_length=13),
        ),
        migrations.AddField(
            model_name='request',
            name='video_contents',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
