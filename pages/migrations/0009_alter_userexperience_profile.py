# Generated by Django 4.2.8 on 2024-01-19 10:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('pages', '0008_alter_userexperience_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userexperience',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.profile'),
        ),
    ]
