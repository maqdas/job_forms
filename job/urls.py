from django.urls import path

from . import views

app_name = 'job'

urlpatterns = [
	path('', views.job , name='job'),
	path('check', views.check , name='check'),
]