# Generated by Django 3.2.7 on 2021-09-23 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0008_alter_userprofile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='picture',
            field=models.ImageField(default='default.png', upload_to='uploads/profile_pictures/'),
        ),
    ]
