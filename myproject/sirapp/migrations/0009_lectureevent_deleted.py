# Generated by Django 4.1.11 on 2023-10-10 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sirapp', '0008_otherevent_deleted'),
    ]

    operations = [
        migrations.AddField(
            model_name='lectureevent',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
    ]
