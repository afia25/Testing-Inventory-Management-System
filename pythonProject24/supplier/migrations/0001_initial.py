# Generated by Django 3.2.8 on 2021-10-22 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('sup_id', models.TextField(primary_key=True, serialize=False)),
                ('sup_name', models.CharField(max_length=50)),
                ('sup_email', models.CharField(max_length=50)),
                ('sup_contact', models.CharField(max_length=11)),
            ],
        ),
    ]