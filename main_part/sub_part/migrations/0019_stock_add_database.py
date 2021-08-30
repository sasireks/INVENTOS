# Generated by Django 3.2.5 on 2021-08-19 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sub_part', '0018_purchase_add_database'),
    ]

    operations = [
        migrations.CreateModel(
            name='stock_add_database',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_warehouse', models.CharField(max_length=100)),
                ('to_warehouse', models.CharField(max_length=100)),
                ('shipping_cost', models.CharField(max_length=100)),
                ('select_state', models.CharField(max_length=100)),
                ('product_name', models.CharField(max_length=100)),
                ('quantatity', models.CharField(max_length=100)),
                ('unit_price', models.CharField(max_length=100)),
                ('product_image', models.CharField(max_length=100)),
            ],
        ),
    ]
