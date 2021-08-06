# Generated by Django 2.0.13 on 2021-07-31 04:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0015_auto_20210731_1028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coworker',
            name='coworker_id',
            field=models.ForeignKey(blank=True, default='admin', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='coworker_id',
            field=models.ForeignKey(blank=True, default='admin', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='request',
            name='coworker',
            field=models.ForeignKey(blank=True, default='admin', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
