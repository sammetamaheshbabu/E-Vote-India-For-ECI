# Generated by Django 5.0.3 on 2024-04-07 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0009_alter_newvoteregistrationdata_resident_since'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newvoteregistrationdata',
            old_name='other_document_type',
            new_name='address_document_type',
        ),
        migrations.RenameField(
            model_name='newvoteregistrationdata',
            old_name='epicNumber',
            new_name='familyepicNumber',
        ),
        migrations.AddField(
            model_name='newvoteregistrationdata',
            name='dob_document_type',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]