# Generated by Django 4.1.1 on 2022-10-05 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_remove_customuser_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='username',
            field=models.CharField(default='admin', max_length=25, verbose_name='admin'),
        ),
    ]