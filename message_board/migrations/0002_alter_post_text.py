# Generated by Django 4.2.14 on 2024-07-25 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message_board', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(max_length=200),
        ),
    ]