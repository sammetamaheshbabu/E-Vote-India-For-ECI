# Generated by Django 5.0.3 on 2024-04-04 00:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polling', '0005_rename_polling_poll'),
    ]

    operations = [
        migrations.RenameField(
            model_name='poll',
            old_name='email',
            new_name='email_id',
        ),
    ]