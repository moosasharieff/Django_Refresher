# Generated by Django 4.2.6 on 2023-10-11 11:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('level_five', '0002_alter_userprofileinfo_profile_pic'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofileinfo',
            old_name='profile_site',
            new_name='portfolio_site',
        ),
    ]
