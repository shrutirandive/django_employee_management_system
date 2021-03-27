# Generated by Django 3.1.7 on 2021-03-24 06:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('male', 'MALE'), ('female', 'FEMALE')], default='MALE', max_length=10)),
                ('jobtitle', models.CharField(max_length=100)),
                ('organization', models.CharField(choices=[('google', 'GOOGLE'), ('microsoft', 'MICROSOFT')], max_length=10)),
                ('dob', models.DateField(default=datetime.datetime.today)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]
