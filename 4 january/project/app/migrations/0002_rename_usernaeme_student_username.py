# Generated by Django 5.1.4 on 2025-01-07 10:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='usernaeme',
            new_name='username',
        ),
    ]
