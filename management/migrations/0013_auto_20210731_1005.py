# Generated by Django 2.0.13 on 2021-07-31 01:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0012_auto_20210731_0952'),
    ]

    operations = [
        migrations.RenameField(
            model_name='introduce',
            old_name='image_url1',
            new_name='image1',
        ),
        migrations.RenameField(
            model_name='introduce',
            old_name='image_url2',
            new_name='image2',
        ),
    ]