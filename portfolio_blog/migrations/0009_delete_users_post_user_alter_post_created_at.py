# Generated by Django 4.1.5 on 2023-01-22 00:26

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('portfolio_blog', '0008_alter_post_created_at_alter_users_created_at'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Users',
        ),
        migrations.AddField(
            model_name='post',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 22, 0, 26, 30, 54583, tzinfo=datetime.timezone.utc)),
        ),
    ]
