# Generated by Django 2.0 on 2020-03-16 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0017_cartx_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordermastertbl',
            name='BillingAddress',
        ),
        migrations.AddField(
            model_name='ordermastertbl',
            name='Email',
            field=models.EmailField(default='abc@gmail.com', max_length=254),
        ),
        migrations.AddField(
            model_name='ordermastertbl',
            name='add1',
            field=models.CharField(default='add1', max_length=100),
        ),
        migrations.AddField(
            model_name='ordermastertbl',
            name='add2',
            field=models.CharField(default='add2', max_length=100),
        ),
        migrations.AddField(
            model_name='ordermastertbl',
            name='city',
            field=models.CharField(default='city', max_length=20),
        ),
        migrations.AddField(
            model_name='ordermastertbl',
            name='cname',
            field=models.CharField(default='cname', max_length=15),
        ),
        migrations.AddField(
            model_name='ordermastertbl',
            name='fname',
            field=models.CharField(default='fname', max_length=15),
        ),
        migrations.AddField(
            model_name='ordermastertbl',
            name='lname',
            field=models.CharField(default='lname', max_length=15),
        ),
        migrations.AddField(
            model_name='ordermastertbl',
            name='phone',
            field=models.IntegerField(default=11),
        ),
        migrations.AddField(
            model_name='ordermastertbl',
            name='postcode',
            field=models.IntegerField(default=11),
        ),
        migrations.AddField(
            model_name='ordermastertbl',
            name='state',
            field=models.CharField(default='state', max_length=20),
        ),
        migrations.AlterField(
            model_name='ordermastertbl',
            name='BillTotal',
            field=models.IntegerField(default=11),
        ),
    ]