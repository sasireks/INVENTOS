# Generated by Django 3.2.5 on 2021-08-04 11:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sub_part', '0006_alter_user_add_database_email_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user_add_database',
            old_name='email_id',
            new_name='email',
        ),
    ]
