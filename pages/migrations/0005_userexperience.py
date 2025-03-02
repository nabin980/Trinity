# Generated by Django 4.2.8 on 2024-01-18 14:15

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('pages', '0004_quotationrequest_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserExperience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=300)),
                ('occupation', models.CharField(max_length=100)),
                ('stars', models.IntegerField(default=0)),
                ('comment', models.TextField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.profile')),
            ],
        ),
    ]
