# Generated by Django 2.0.13 on 2021-07-30 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0008_auto_20210731_0138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='introduce',
            name='image_url1',
            field=models.CharField(default='orange.svg', max_length=400),
        ),
        migrations.AlterField(
            model_name='introduce',
            name='image_url2',
            field=models.CharField(default='orange.svg', max_length=400),
        ),
        migrations.AlterField(
            model_name='introduce',
            name='title_big',
            field=models.CharField(default='제목', max_length=400),
        ),
    ]
