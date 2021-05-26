# Generated by Django 2.0.4 on 2018-05-07 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('address', models.TextField()),
                ('timeline', models.TextField()),
                ('dressCode', models.TextField()),
                ('duration', models.DurationField()),
                ('date', models.DateTimeField()),
            ],
        ),
    ]