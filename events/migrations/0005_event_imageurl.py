# Generated by Django 3.2.3 on 2021-06-02 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_auto_20210601_2159'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='ImageURL',
            field=models.CharField(default='https://i.imgur.com/CcY947L.jpg', max_length=255),
        ),
    ]
