# Generated by Django 4.2.6 on 2023-10-10 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('level_five', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='profile_pic',
            field=models.ImageField(blank=True, upload_to='profile_pic'),
        ),
    ]
