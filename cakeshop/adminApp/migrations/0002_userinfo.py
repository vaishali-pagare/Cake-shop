# Generated by Django 4.1.2 on 2022-11-13 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='userInfo',
            fields=[
                ('uname', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=20)),
                ('emails', models.EmailField(max_length=100)),
            ],
            options={
                'db_table': 'userInfo',
            },
        ),
    ]
