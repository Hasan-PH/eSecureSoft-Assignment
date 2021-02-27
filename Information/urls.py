from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from . import views

urlpatterns = [
url(r'^$', views.registration, name='registration'),
url(r'^list/', views.list, name='list'),

path('ajax/load-teacher/', views.load_teacher, name='ajax_load_cities'), # AJAX
]
