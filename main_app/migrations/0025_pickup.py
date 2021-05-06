# Generated by Django 2.0 on 2020-03-24 06:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0024_serviceaccept_servicereject'),
    ]

    operations = [
        migrations.CreateModel(
            name='pickup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(default='', max_length=13)),
                ('vehid', models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='main_app.serviceaccept')),
            ],
        ),
    ]