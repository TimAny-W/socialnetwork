# Generated by Django 4.1.1 on 2022-10-16 21:11

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_customuser_friends_list'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='friends_list',
        ),
        migrations.AddField(
            model_name='customuser',
            name='friends_list',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
