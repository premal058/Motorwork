# Generated by Django 2.0 on 2020-03-20 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0019_orderdetails_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='Usedvehicle_photo',
            field=models.ImageField(default='patient_icon.png', upload_to='main_app/static/main_app/img/user'),
        ),
    ]