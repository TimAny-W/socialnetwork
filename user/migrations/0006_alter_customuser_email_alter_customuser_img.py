# Generated by Django 4.1.1 on 2022-10-11 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_alter_customuser_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='Email address'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='img',
            field=models.ImageField(default='user/default_avatar.png', upload_to='user/<django.db.models.fields.EmailField>/', verbose_name='Avatar'),
        ),
    ]
