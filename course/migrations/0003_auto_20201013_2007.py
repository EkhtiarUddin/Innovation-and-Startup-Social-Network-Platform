# Generated by Django 3.1.1 on 2020-10-13 20:07

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('course', '0002_auto_20201007_0241'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enroll',
            name='enrolls',
        ),
        migrations.RemoveField(
            model_name='enroll',
            name='enrolluser',
        ),
        migrations.AddField(
            model_name='enroll',
            name='user',
            field=models.ManyToManyField(related_name='enrollingUser', to=settings.AUTH_USER_MODEL),
        ),
    ]
