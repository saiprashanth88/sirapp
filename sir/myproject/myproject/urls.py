
from django.contrib import admin
from django.urls import path
from django.urls import include
from sirapp import views
from sirapp.views import GeneratePDF
# from . import views
urlpatterns = [
    path('', views.index, name='home'),
    path('admin_registration/', views.admin_registration, name='admin_registration'),
    path('admin_login/', views.admin_login, name='admin_login'),
    path('registration/', views.registration, name='registration'),
    path('liveevents/', views.liveevents, name='liveevents'),
    path('requestform/', views.requestform, name='requestform'),
    path('studentevents/', views.studentevents, name='studentevents'),
    path('lectures_seminar/', views.lectures_seminar, name='lectures_seminar'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('user_home/',views.user_home,name = 'user_home'),
    path('faculty/',views.facultyevents,name= "facultyevents"),
    path('admin_lectures/',views.admin_lectures, name = "admin_lectures"),
    path('admin_fac_events/',views.admin_fac_events,name="admin_fac_events"),
    path('admin_std_events/',views.admin_std_events,name="admin_std_events"),
    path('admin_calender/',views.admin_calender, name="admin_calender"),
    path('admin_settings/', views.admin_settings, name="admin_settings"),
    path('submit_feedback/', views.submit_feedback, name='submit_feedback'),
    path('submit_lecture_feedback/', views.submit_lecture_feedback, name='submit_lecture_feedback'),
    path('submit_faculty_event_feedback/',views.submit_faculty_event_feedback,name='submit_faculty_event_feedback'),


    path('feedback/<str:event_title>/', views.feedback_page, name='feedback_page'),
    path('std_feedback/<str:event_title>/', views.std_feedbacks, name='std_feedbacks'),
    path('fac_feedback/<str:event_title>/', views.fac_feedbacks, name='fac_feedbacks'),
    path('std_login/',views.std_login, name ="std_login"),
    path('fac_login/',views.fac_login, name ="fac_login"),
    path('lec_login/',views.lec_login, name ="lec_login"),
    # path('generate_pdf/<str:event_title>/',views.GeneratePDF, name='generate_pdf'),
    path('generate_pdf/<str:event_title>/', GeneratePDF.as_view(), name='generate_pdf'),
    path('pdf_template/',views.pdf_template, name="pdf_template"),
    path('admin_request/',views.admin_request, name="admin_request"),













]
