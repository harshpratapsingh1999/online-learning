# Generated by Django 4.0.3 on 2022-04-11 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('email', models.TextField(max_length=50)),
                ('role', models.CharField(max_length=10)),
                ('log_token', models.TextField(max_length=50)),
                ('limit', models.IntegerField()),
            ],
        ),
    ]
