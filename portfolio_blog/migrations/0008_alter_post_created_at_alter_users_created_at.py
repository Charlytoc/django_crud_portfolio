# Generated by Django 4.1.5 on 2023-01-22 00:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_blog', '0007_users_alter_post_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 22, 0, 10, 9, 706567, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='users',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 22, 0, 10, 9, 706567, tzinfo=datetime.timezone.utc)),
        ),
    ]