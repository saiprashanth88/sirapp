# Generated by Django 4.1.11 on 2023-09-14 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sirapp', '0013_typeofuser_userrequest'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClgParticipantType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ClgRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('program_type', models.CharField(max_length=255)),
                ('program_topic', models.CharField(blank=True, max_length=255, null=True)),
                ('program_duration', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('start_time', models.TimeField(blank=True, null=True)),
                ('end_time', models.TimeField(blank=True, null=True)),
                ('course', models.CharField(max_length=255)),
                ('year', models.CharField(max_length=255)),
                ('branch', models.CharField(max_length=255)),
                ('semester', models.CharField(max_length=255)),
                ('mobile', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('terms_and_conditions', models.BooleanField()),
                ('participants_type', models.ManyToManyField(to='sirapp.clgparticipanttype')),
            ],
        ),
    ]
