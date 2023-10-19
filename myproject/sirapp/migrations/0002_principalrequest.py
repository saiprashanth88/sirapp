# Generated by Django 4.1.11 on 2023-09-20 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sirapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrincipalRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('college_name', models.CharField(max_length=200)),
                ('day', models.CharField(max_length=200)),
                ('date', models.DateField()),
                ('mode', models.CharField(choices=[('Offline', 'Offline'), ('Online', 'Online')], max_length=100)),
                ('participants', models.IntegerField()),
                ('contact_name', models.CharField(max_length=200)),
                ('institution', models.CharField(max_length=100)),
                ('mobile', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('program_type', models.CharField(choices=[('Faculty Development Program', 'Faculty Development Program'), ('Student Development Program', 'Student Development Program')], max_length=100)),
                ('topic_guest', models.CharField(blank=True, max_length=100, null=True)),
                ('duration_guest', models.CharField(blank=True, max_length=100, null=True)),
                ('from_time_guest', models.CharField(blank=True, max_length=100, null=True)),
                ('to_time_guest', models.CharField(blank=True, max_length=100, null=True)),
                ('participant_type_guest', models.CharField(blank=True, choices=[('Students', 'Students'), ('Faculty', 'Faculty')], max_length=100, null=True)),
                ('course_guest', models.CharField(blank=True, max_length=200, null=True)),
                ('year', models.CharField(blank=True, max_length=100, null=True)),
                ('branch', models.CharField(blank=True, max_length=100, null=True)),
                ('semester', models.CharField(blank=True, max_length=100, null=True)),
                ('topic_faculty', models.CharField(blank=True, max_length=100, null=True)),
                ('duration_faculty', models.CharField(blank=True, max_length=100, null=True)),
                ('from_time_faculty', models.CharField(blank=True, max_length=100, null=True)),
                ('to_time_faculty', models.CharField(blank=True, max_length=100, null=True)),
                ('topic_student', models.CharField(blank=True, max_length=100, null=True)),
                ('duration_student', models.CharField(blank=True, max_length=100, null=True)),
                ('course', models.CharField(blank=True, max_length=200, null=True)),
                ('student_year', models.CharField(blank=True, max_length=100, null=True)),
                ('student_branch', models.CharField(blank=True, max_length=100, null=True)),
                ('student_semester', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
