# Generated by Django 5.0.3 on 2024-04-03 20:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_loginvoter_rename_voter_signupvoter'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SignUpVoter',
            new_name='voter',
        ),
        migrations.DeleteModel(
            name='LoginVoter',
        ),
    ]
