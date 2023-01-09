# Generated by Django 4.1.2 on 2022-11-20 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminApp', '0002_userinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cardno', models.CharField(max_length=20)),
                ('cvv', models.CharField(max_length=4)),
                ('expiry', models.CharField(max_length=20)),
                ('balance', models.FloatField(default=1000)),
            ],
            options={
                'db_table': 'Payment',
            },
        ),
    ]
