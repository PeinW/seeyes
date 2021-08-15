# Generated by Django 2.2.17 on 2021-03-21 12:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20210321_1249'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='location',
        ),
        migrations.RemoveField(
            model_name='user',
            name='stats',
        ),
        migrations.RemoveField(
            model_name='user',
            name='type',
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stats', models.CharField(blank=True, max_length=10, null=True)),
                ('type', models.CharField(blank=True, max_length=10, null=True)),
                ('location', models.CharField(blank=True, max_length=10, null=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]