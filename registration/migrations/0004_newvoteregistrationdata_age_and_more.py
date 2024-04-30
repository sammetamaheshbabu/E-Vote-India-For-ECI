# Generated by Django 5.0.3 on 2024-04-01 10:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0003_newvoteregistrationdata_delete_aadhaardetails_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='newvoteregistrationdata',
            name='age',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='newvoteregistrationdata',
            name='date_of_birth',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='newvoteregistrationdata',
            name='father_name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='newvoteregistrationdata',
            name='first_name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='newvoteregistrationdata',
            name='full_name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='newvoteregistrationdata',
            name='middle_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='newvoteregistrationdata',
            name='mother_name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='newvoteregistrationdata',
            name='photo',
            field=models.ImageField(default='', max_length=255, upload_to='photos/'),
        ),
        migrations.AddField(
            model_name='newvoteregistrationdata',
            name='surname',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='newvoteregistrationdata',
            name='email_id',
            field=models.EmailField(default='', max_length=254),
        ),
        migrations.AlterField(
            model_name='newvoteregistrationdata',
            name='mobile_number',
            field=models.CharField(default='', max_length=15),
        ),
        migrations.AlterField(
            model_name='newvoteregistrationdata',
            name='relative_name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='newvoteregistrationdata',
            name='relative_surname',
            field=models.CharField(default='', max_length=100),
        ),
    ]
