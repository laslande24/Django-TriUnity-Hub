# Generated by Django 4.2.3 on 2023-07-26 07:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('body', models.CharField(max_length=100000000)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2023, 7, 26, 8, 42, 25, 658030))),
            ],
        ),
        migrations.DeleteModel(
            name='posts',
        ),
    ]
