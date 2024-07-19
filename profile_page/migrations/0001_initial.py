# Generated by Django 4.2.14 on 2024-07-18 10:55

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_picture', cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image')),
                ('about_me', models.TextField()),
                ('join_date', models.DateTimeField(auto_now_add=True)),
                ('Display_name', models.CharField(max_length=12, unique=True)),
                ('high_score', models.IntegerField(default=0)),
            ],
        ),
    ]