# Generated by Django 2.0.13 on 2021-07-31 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0010_auto_20210731_0947'),
    ]

    operations = [
        migrations.AddField(
            model_name='introduce',
            name='image_url2',
            field=models.ImageField(default='static/management/orange.svg', upload_to=''),
        ),
        migrations.AlterField(
            model_name='introduce',
            name='image_url1',
            field=models.ImageField(default='static/management/orange.svg', upload_to=''),
        ),
    ]
