# Generated by Django 4.2.8 on 2024-01-19 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0010_userexperience_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='userexperience',
            name='is_published',
            field=models.BooleanField(default=False),
        ),
    ]
