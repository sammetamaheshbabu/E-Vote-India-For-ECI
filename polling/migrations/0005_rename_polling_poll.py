# Generated by Django 5.0.3 on 2024-04-03 23:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polling', '0004_remove_polling_captcha_text'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='polling',
            new_name='poll',
        ),
    ]
