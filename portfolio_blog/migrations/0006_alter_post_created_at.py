# Generated by Django 4.1.5 on 2023-01-21 23:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_blog', '0005_alter_post_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 21, 23, 23, 44, 534733, tzinfo=datetime.timezone.utc)),
        ),
    ]