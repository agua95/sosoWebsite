# Generated by Django 2.2.7 on 2019-11-13 22:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20191113_1425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 13, 14, 48, 29, 103066), verbose_name='date published'),
        ),
    ]
