# Generated by Django 4.0.3 on 2022-04-12 05:02

import builtins
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_user_details'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_details',
            name='photo',
            field=models.BinaryField(default=1, verbose_name=builtins.max),
            preserve_default=False,
        ),
    ]
