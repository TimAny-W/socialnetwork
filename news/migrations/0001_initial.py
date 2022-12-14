# Generated by Django 4.1.1 on 2022-10-11 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=75, verbose_name='title')),
                ('announce', models.CharField(max_length=255, verbose_name='announce')),
                ('text', models.TextField(verbose_name='text')),
                ('img', models.ImageField(null=True, upload_to='', verbose_name='image')),
                ('date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
