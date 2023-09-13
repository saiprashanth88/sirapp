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

class LectureEventFeedback(models.Model):
    event = models.ForeignKey(LectureEvent, on_delete=models.CASCADE, related_name='feedback')
    name = models.CharField(max_length=255)
    email = models.EmailField()
    feedback = models.TextField()

    def __str__(self):
        return f"Feedback for {self.event.title} on {self.event.date}"

class FacultyEventFeedback(models.Model):
    event = models.ForeignKey(FacultyEvent, on_delete=models.CASCADE, related_name='feedback')
    name = models.CharField(max_length=255)
    email = models.EmailField()
    feedback_text = models.TextField()

    def __str__(self):
        return f"Feedback for {self.event.title} on {self.event.date}"


class StudentEventFeedback(models.Model):
    event = models.ForeignKey(StudentEvent, on_delete=models.CASCADE, related_name='feedback')
    name = models.CharField(max_length=255)
    email = models.EmailField()
    feedback = models.TextField()

    def __str__(self):
        return f"Feedback for {self.event.title} on {self.event.date}"

class OtherEvent(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateField()
    location = models.CharField(max_length=255)
    contact_person = models.CharField(max_length=255)
    email = models.EmailField()
    cell = models.CharField(max_length=20)
    description = models.TextField()

    def __str__(self):
        return self.title

class OtherEventFeedback(models.Model):
    event = models.ForeignKey(OtherEvent, on_delete=models.CASCADE, related_name='feedback')
    name = models.CharField(max_length=255)
    email = models.EmailField()
    feedback = models.TextField()

    def __str__(self):
        return f"Feedback for {self.event.title} on {self.event.date}"


class RequestFormSubmission(models.Model):
    date = models.DateField()
    program_type = models.CharField(max_length=100)
    program_topic = models.CharField(max_length=255, blank=True, null=True)
    program_duration = models.FloatField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    participants_type = models.ManyToManyField('ParticipantType', blank=True)
    course = models.CharField(max_length=100)
    year = models.CharField(max_length=10)
    branch = models.CharField(max_length=100)
    semester = models.CharField(max_length=10)
    mobile = models.CharField(max_length=10)
    email = models.EmailField()
    terms_and_conditions = models.BooleanField()

    def __str__(self):
        return f'Request Form Submission by {self.email}'
class ParticipantType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
