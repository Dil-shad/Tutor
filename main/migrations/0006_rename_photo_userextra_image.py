# Generated by Django 4.0.4 on 2022-05-09 17:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_userextra_mobile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userextra',
            old_name='photo',
            new_name='image',
        ),
    ]
