# Generated by Django 2.0 on 2020-04-06 17:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0038_updates'),
    ]

    operations = [
        migrations.CreateModel(
            name='chat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=200)),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.User')),
            ],
        ),
    ]
