# Generated by Django 3.2.8 on 2021-10-23 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20211023_1508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='quantity',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='total',
            field=models.IntegerField(),
        ),
    ]