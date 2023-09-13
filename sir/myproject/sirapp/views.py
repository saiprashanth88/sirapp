from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import UserRegistration
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import StudentEvent, FacultyEvent, LectureEvent,LectureEventFeedback
from django.db.models import Count
import calendar
from .models import StudentEvent, StudentEventFeedback
from django.http import JsonResponse
from .models import FacultyEventFeedback,OtherEvent, OtherEventFeedback,RequestFormSubmission,ParticipantType
import csv
from django.http import HttpResponse
from django.template.loader import get_template
from django.views import View
from xhtml2pdf import pisa  # Importing the module for pdf creation

def pdf_template(request):
    return render(request, "pdf_template")

class GeneratePDF(View):
    def get(self, request, event_title):
        # Get the feedback data for the specified event
        feedbacks = LectureEventFeedback.objects.filter(event__title=event_title)

        # Create a PDF template using Django's template system
        template = get_template('pdf_template.html')
        context = {'feedbacks': feedbacks, 'event_title': event_title}
        html = template.render(context)

        # Create a PDF response
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="{event_title}_feedback.pdf"'

        # Generate the PDF and write it to the response
        pisa_status = pisa.CreatePDF(html, dest=response)
        if pisa_status.err:
            return HttpResponse('PDF generation error')

        return response

# Import any models or forms you may have here

# views.py
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

def get_user_credentials():
    # Retrieve all UserRegistration objects from the database
    user_records = UserRegistration.objects.all()

    # Create a dictionary to store email-password pairs
    user_credentials = {}

    # Populate the dictionary with email-password pairs from the database records
    for user_record in user_records:
        user_credentials[user_record.email] = user_record.password

    return user_credentials

def admin_login(request):
    if request.method == 'POST':
        user_type = request.POST['userType']
        email = request.POST['email']
        password = request.POST['password']

        # Check if the user exists and is of the selected type
        mydict = dict()
        mydict = get_user_credentials()
        print(mydict)
        try:

          if user_type == "admin" and email=="prof_saikumar@rediffmail.com" and password == "12345":
              return redirect('dashboard')
          elif password == mydict[email]:
              return redirect('user_home')
          else:
              error_message = 'Invalid email, password, or user type. Please try again.'
              return render(request, 'admin_login.html', {'error_message': error_message})
        except:

          error_message = 'Invalid email, password, or user type. Please try again.'
          return render(request, 'admin_login.html', {'error_message': error_message})

    return render(request, 'admin_login.html')

def index(request):
    return render(request, "home.html")


def admin_registration(request):
  if request.method == 'POST':
      email = request.POST['regEmail']
      password = request.POST['regPassword']
      confirm_password = request.POST['confirmPassword']

      if password != confirm_password:
          messages.error(request, "Passwords do not match.")
          return redirect('admin_registration')

      if UserRegistration.objects.filter(email=email).exists():
          messages.error(request, "Email already registered.")
          return redirect('admin_registration')

      # Create a new user registration record
      user_registration = UserRegistration(email=email, password=password)
      user_registration.save()

      messages.success(request, "Registration successful. You can now log in.")
      return redirect('admin_login')  # Redirect to the login page after successful registration

  return render(request, "admin_registration.html")



def lectures_seminar(request):
    months_years = LectureEvent.objects.dates('date', 'month')

    # Create a dictionary to store events grouped by month and year
    events_by_month = {}
    for date in months_years:
        month = date.strftime('%B')
        year = date.year
        events = LectureEvent.objects.filter(date__month=date.month, date__year=year)
        events_by_month[(month, year)] = events

    return render(request, 'lectures_seminar.html', {'events_by_month': events_by_month})


def studentevents(request):
    months_years = StudentEvent.objects.dates('date', 'month')

    # Create a dictionary to store events grouped by month and year
    events_by_month = {}
    for date in months_years:
        month = date.strftime('%B')
        year = date.year
        events = StudentEvent.objects.filter(date__month=date.month, date__year=year)
        events_by_month[(month, year)] = events

    return render(request, 'studentevents.html', {'events_by_month': events_by_month})

def liveevents(request):
    return render(request, "liveevents.html")

def requestform(request):
    return render(request, "requestform.html")

def registration(request):
    return render(request, 'admin_registration.html')

def dashboard(request):
    return render(request,"dashboard.html")

def user_home(request):
    return render(request,"user_home.html")

def facultyevents(request):
    # Get distinct months and years from the 'date' field of FacultyEvent model
    months_year = OtherEvent.objects.dates('date', 'month')

    # Create a dictionary to store events grouped by month and year
    events_by_month = {}
    for date in months_year:
        month = date.strftime('%B')
        year = date.year
        events = OtherEvent.objects.filter(date__month=date.month, date__year=year).order_by('-date')
        events_by_month[(month, year)] = events

    return render(request, 'facultyevents.html', {'events_by_month': events_by_month})
def admin_lectures(request):
    if request.method == 'POST':
        # Process and save the form data to the database
        title = request.POST['title']
        date = request.POST['date']
        location = request.POST['college']
        contact_person = request.POST['location']
        email = request.POST['email']
        cell = request.POST['cell']
        description = request.POST['description']

        # Save the data to the LectureEvent model
        lecture_event = LectureEvent(title=title, date=date, location=location, contact_person=contact_person, email=email, cell=cell, description=description)
        lecture_event.save()

        # Show a success message
        messages.success(request, "Lecture or seminar details added successfully.")

        # Redirect to the same page to display the success message
        return redirect('admin_lectures')
    lecture_events = LectureEvent.objects.all()

    context = {
        'lecture_events': lecture_events,
    }

    return render(request, 'admin_lectures.html', context)




def admin_fac_events(request):
    if request.method == 'POST':
        # Process and save the form data to the database
        title = request.POST['title']
        date = request.POST['date']
        location = request.POST['college']
        contact_person = request.POST['location']
        email = request.POST['email']
        cell = request.POST['cell']
        description = request.POST['description']

        # Save the data to the FacultyEvent model
        faculty_event = OtherEvent(title=title, date=date, location=location, contact_person=contact_person, email=email, cell=cell, description=description)
        faculty_event.save()

        # Show a success message
        messages.success(request, "Faculty event details added successfully.")

        # Redirect to the same page to display the success message
    faculty_events = OtherEvent.objects.all()

    context = {
        'faculty_events': faculty_events,
    }

    return render(request, 'admin_fac_events.html', context)

def admin_std_events(request):
    if request.method == 'POST':
        # Process and save the form data to the database
        title = request.POST['title']
        date = request.POST['date']
        college = request.POST['college']
        location = request.POST['location']
        description = request.POST['description']



        # Save the data to the StudentEvent model
        student_event = StudentEvent(title=title, date=date, college=college, location=location, description=description)
        student_event.save()


        # Show a success message
        messages.success(request, "Student event details added successfully.")

        # Redirect to the same page to display the success message
        # return redirect('admin_std_events')

    student_events = StudentEvent.objects.all()

    context = {
        'student_events': student_events,
    }

    return render(request, 'admin_std_events.html', context)

def submit_feedback(request):
    if request.method == 'POST':
        event_title = request.POST.get('event_title')
        name = request.POST.get('name')
        email = request.POST.get('email')
        feedback_text = request.POST.get('feedback_text')

        # Get the event based on the title
        event = StudentEvent.objects.get(title=event_title)

        # Create and save the feedback
        feedback = StudentEventFeedback(event=event, name=name, email=email, feedback=feedback_text)
        feedback.save()

    return redirect('studentevents')
def submit_lecture_feedback(request):
    if request.method == 'POST':
        event_title = request.POST.get('event_title')
        name = request.POST.get('name')
        email = request.POST.get('email')
        feedback_text = request.POST.get('feedback_text')

        # Get the event based on the title
        event = LectureEvent.objects.get(title=event_title)

        # Create and save the feedback
        feedback = LectureEventFeedback(event=event, name=name, email=email, feedback=feedback_text)
        feedback.save()

    return redirect('lectures_seminar')
def submit_faculty_event_feedback(request):
    if request.method == 'POST':

        event_title = request.POST.get('event_title')
        name = request.POST.get('name')
        email = request.POST.get('email')
        feedback_text = request.POST.get('feedback_text')

        # Get the event based on the title
        event = OtherEvent.objects.get(title=event_title)

        # Create and save the feedback
        feedback = OtherEventFeedback(event=event, name=name, email=email, feedback=feedback_text)
        feedback.save()

        # Redirect to a thank you page or any other appropriate page

    return redirect('facultyevents')







def admin_calender(request):
    return render(request, "admin_calender.html")

def admin_settings(request):
    return render(request, "admin_settings.html")


def feedback_page(request, event_title):
    # Assuming that event_title corresponds to the event's title in LectureEvent model
    feedbacks = LectureEventFeedback.objects.filter(event__title=event_title)
    context = {'feedbacks': feedbacks,'event_title':event_title}
    return render(request, 'feedback_page.html', context)


def std_feedbacks(request, event_title):
    feedbacks = StudentEventFeedback.objects.filter(event__title=event_title)
    context = {'feedbacks':feedbacks,'event_title':event_title}
    return render(request,'std_feedbacks.html',context)



def fac_feedbacks(request, event_title):
    feedbacks = OtherEventFeedback.objects.filter(event__title=event_title)
    context = {'feedbacks':feedbacks,'event_title':event_title}
    return render(request,'fac_feedbacks.html',context)


def std_login(request):
    months_years = StudentEvent.objects.dates('date', 'month')

    # Create a dictionary to store events grouped by month and year
    events_by_month = {}
    for date in months_years:
        month = date.strftime('%B')
        year = date.year
        events = StudentEvent.objects.filter(date__month=date.month, date__year=year)
        events_by_month[(month, year)] = events

    return render(request, 'std_login.html', {'events_by_month': events_by_month})

def fac_login(request):
    months_year = OtherEvent.objects.dates('date', 'month')

    # Create a dictionary to store events grouped by month and year
    events_by_month = {}
    for date in months_year:
        month = date.strftime('%B')
        year = date.year
        events = OtherEvent.objects.filter(date__month=date.month, date__year=year).order_by('-date')
        events_by_month[(month, year)] = events

    return render(request, 'fac_login.html', {'events_by_month': events_by_month})

def lec_login(request):
    months_years = LectureEvent.objects.dates('date', 'month')

    # Create a dictionary to store events grouped by month and year
    events_by_month = {}
    for date in months_years:
        month = date.strftime('%B')
        year = date.year
        events = LectureEvent.objects.filter(date__month=date.month, date__year=year)
        events_by_month[(month, year)] = events

    return render(request, 'lec_login.html', {'events_by_month': events_by_month})


def admin_request(request):
    if request.method == 'POST':
        # Get data from the request
        date = request.POST.get('date')
        program_type = request.POST.get('program_type')
        program_topic = request.POST.get('program_topic')
        program_duration = request.POST.get('program_duration')
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')
        participants_type = request.POST.getlist('participants_type')
        course = request.POST.get('course')
        year = request.POST.get('year')
        branch = request.POST.get('branch')
        semester = request.POST.get('semester')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        terms_and_conditions = request.POST.get('terms_and_conditions')

        # Create a new RequestFormSubmission object and save it
        submission = RequestFormSubmission(
            date=date,
            program_type=program_type,
            program_topic=program_topic,
            program_duration=program_duration,
            start_time=start_time,
            end_time=end_time,
            course=course,
            year=year,
            branch=branch,
            semester=semester,
            mobile=mobile,
            email=email,
            terms_and_conditions=terms_and_conditions
        )
        submission.save()

    # Get ParticipantType objects by their names
        participant_types = ParticipantType.objects.filter(name__in=participants_type)

        # Set the ManyToMany field with the obtained ParticipantType objects
        submission.participants_type.set(participant_types)


    return render(request, 'request_form.html')


