from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import UserRegistration
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import StudentEvent, FacultyEvent, LectureEvent

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

# def admin_login(request):
#     if request.method == 'POST':
#         email = request.POST['email']
#         password = request.POST['password']
#         user_type = request.POST['userType']

#         # Check if the user exists and is of the selected type
#         user = User.objects.filter(email=email, user_type=user_type).first()

#         if user is not None:
#             # Use Django's built-in authentication to check the password
#             authenticated_user = authenticate(request, username=user.username, password=password)
#             if authenticated_user is not None:
#                 # Log the user in
#                 login(request, authenticated_user)
#                 if user_type == 'Admin':
#                     return redirect('dashboard')
#                 elif user_type == 'User':
#                     return redirect('user_home')

#         # Display an error message if login fails
#         error_message = 'Invalid email, password, or user type. Please try again.'
#         return render(request, 'admin_login.html', {'error_message': error_message})

#     return render(request, 'admin_login.html')

def lectures_seminar(request):
    return render(request, "lectures_seminar.html")


def studentevents(request):
    return render(request, "studentevents.html")

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
    return render(request, "facultyevents.html")

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

    return render(request, "admin_lectures.html")

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
        faculty_event = FacultyEvent(title=title, date=date, location=location, contact_person=contact_person, email=email, cell=cell, description=description)
        faculty_event.save()

        # Show a success message
        messages.success(request, "Faculty event details added successfully.")

        # Redirect to the same page to display the success message
        return redirect('admin_fac_events')

    return render(request, "admin_fac_events.html")
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

    return render(request, "admin_std_events.html")

def admin_calender(request):
    return render(request, "admin_calender.html")

def admin_settings(request):
    return render(request, "admin_settings.html")
