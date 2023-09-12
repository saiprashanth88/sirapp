
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


]
