# Generated by Django 4.1.5 on 2023-01-21 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Posta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
