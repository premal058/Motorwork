# Generated by Django 2.0 on 2020-03-21 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0022_auto_20200321_1235'),
    ]

    operations = [
        migrations.AddField(
            model_name='foreman',
            name='Foreman_photo',
            field=models.ImageField(default='main_app/static/main_app/img/avtar.jpg', upload_to='main_app/static/main_app/img/foreman'),
        ),
    ]
