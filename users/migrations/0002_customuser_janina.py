# Generated by Django 5.1.3 on 2024-11-22 03:46

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='janina',
            field=models.CharField(default=django.utils.timezone.now, max_length=200, verbose_name='janina'),
            preserve_default=False,
        ),
    ]
