# Generated by Django 2.0.13 on 2021-07-30 00:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Requests',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contents', models.TextField()),
                ('submitted_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('company', models.TextField()),
            ],
        ),
    ]
