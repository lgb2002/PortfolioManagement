# Generated by Django 2.0.13 on 2021-07-30 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0003_auto_20210730_1224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requests',
            name='company',
            field=models.TextField(max_length=400),
        ),
    ]