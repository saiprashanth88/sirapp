
from django.contrib import admin
from django.urls import path
from django.urls import include
from sirapp import views
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


]
