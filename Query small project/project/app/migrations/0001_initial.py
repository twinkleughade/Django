# Generated by Django 5.2 on 2025-05-07 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=50)),
                ('contact', models.IntegerField()),
                ('city', models.CharField(max_length=20)),
            ],
        ),
    ]
