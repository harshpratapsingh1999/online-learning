# Generated by Django 4.0.3 on 2022-04-11 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='enrollment_details',
            fields=[
                ('enrollment_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('username', models.TextField(max_length=50)),
                ('course_category', models.CharField(max_length=20)),
                ('course_name', models.TextField(max_length=50)),
                ('amount', models.IntegerField()),
                ('course_type', models.CharField(max_length=20)),
                ('payment_mode', models.CharField(max_length=20)),
                ('payment_type', models.CharField(max_length=20)),
                ('course_status', models.CharField(max_length=20)),
            ],
        ),
    ]
