# Generated by Django 3.1.7 on 2021-12-08 02:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('simpleapp', '0004_news_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='category',
        ),
    ]
