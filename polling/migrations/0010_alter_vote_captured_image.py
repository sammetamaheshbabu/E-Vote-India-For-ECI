# Generated by Django 5.0.3 on 2024-04-09 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polling', '0009_vote_captured_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='captured_image',
            field=models.ImageField(upload_to='DataBase/vote_images/'),
        ),
    ]