# Generated by Django 5.2 on 2025-04-24 08:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_baseinfo_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='proxybaseinfo',
            options={'ordering': ['name'], 'verbose_name': 'Myproxymodel'},
        ),
    ]
