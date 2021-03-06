# Generated by Django 3.2.8 on 2021-10-22 10:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=30)),
                ('delivary_address', models.CharField(max_length=150)),
                ('city', models.CharField(max_length=150)),
                ('area', models.CharField(max_length=150)),
                ('contact_number', models.CharField(max_length=150)),
                ('delivery_within_what_time', models.CharField(max_length=150)),
                ('alternative_contact_name', models.CharField(max_length=150)),
                ('alternative_contact_number', models.CharField(max_length=150)),
                ('payment_method', models.CharField(max_length=150)),
                ('profile_picture', models.ImageField(default='default.jpg', upload_to='profile_pictures')),
                ('quantity', models.IntegerField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discount', models.IntegerField()),
                ('delivery_charge', models.IntegerField()),
                ('customer_id', models.CharField(default='', max_length=10)),
                ('total_price', models.IntegerField()),
                ('payment', models.IntegerField()),
                ('due', models.IntegerField()),
                ('total', models.IntegerField(default=0)),
                ('prod_id', models.CharField(default='', max_length=10)),
                ('name_of_product', models.CharField(default='', max_length=50)),
                ('quantity', models.IntegerField(default=0)),
                ('name_of_customer', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.CharField(max_length=10)),
                ('user_id', models.CharField(max_length=10)),
                ('quantity', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(default='', max_length=30)),
                ('category_name', models.CharField(default='', max_length=30)),
                ('description', models.CharField(default='', max_length=100)),
                ('buying_price', models.IntegerField(default=1)),
                ('selling_price', models.IntegerField(default=1)),
                ('purchase', models.IntegerField(default=1)),
                ('sale', models.IntegerField(default=1)),
                ('stock', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='SupplierInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supplier_name', models.CharField(default='', max_length=50)),
                ('supplier_email', models.CharField(default='', max_length=50)),
                ('supplier_contact', models.CharField(default='', max_length=11)),
                ('productId', models.CharField(default='', max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='User_Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('customer_id', models.CharField(default='', max_length=30)),
                ('delivary_address', models.CharField(max_length=150)),
                ('city', models.CharField(max_length=150)),
                ('area', models.CharField(max_length=150)),
                ('contact_number', models.CharField(max_length=150)),
                ('delivery_within_what_time', models.CharField(max_length=150)),
                ('alternative_contact_name', models.CharField(max_length=150)),
                ('alternative_contact_number', models.CharField(max_length=150)),
                ('payment_method', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=30)),
                ('username', models.TextField()),
                ('first_name', models.TextField()),
                ('last_name', models.TextField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pofit', models.IntegerField()),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.customerinfo')),
                ('invoice', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.invoice')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.products')),
            ],
        ),
        migrations.AddField(
            model_name='customerinfo',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.products'),
        ),
    ]
