# Generated by Django 3.2.5 on 2021-08-02 11:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sub_part', '0002_contact_reg'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact_reg',
            old_name='name',
            new_name='user_name',
        ),
    ]
