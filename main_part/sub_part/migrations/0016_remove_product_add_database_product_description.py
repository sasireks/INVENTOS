# Generated by Django 3.2.5 on 2021-08-15 04:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sub_part', '0015_product_add_database'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product_add_database',
            name='product_description',
        ),
    ]