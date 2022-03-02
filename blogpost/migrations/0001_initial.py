# Generated by Django 3.0.2 on 2022-03-02 16:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blogpost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('publish_date', models.DateField(default=datetime.date.today)),
            ],
        ),
    ]
