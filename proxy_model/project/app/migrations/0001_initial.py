# Generated by Django 5.2 on 2025-04-24 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BaseInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('dob', models.DateField()),
                ('address', models.CharField()),
                ('branch', models.CharField()),
                ('fees', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ProxyBaseInfo',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('app.baseinfo',),
        ),
    ]
