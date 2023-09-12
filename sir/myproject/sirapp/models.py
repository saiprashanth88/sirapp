from django.db import models
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

class UserRegistration(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.email
class StudentEvent(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateField()
    college = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title
class FacultyEvent(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateField()
    location = models.CharField(max_length=255)
    contact_person = models.CharField(max_length=255)
    email = models.EmailField()
    cell = models.CharField(max_length=20)
    description = models.TextField()

    def __str__(self):
        return self.title
class LectureEvent(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateField()
    location = models.CharField(max_length=255)
    contact_person = models.CharField(max_length=255)
    email = models.EmailField()
    cell = models.CharField(max_length=20)
    description = models.TextField()

    def __str__(self):
        return self.title

