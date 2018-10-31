from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'webapp'
urlpatterns = [
    path('', views.index, name='index'),
    url('input', views.input, name = 'input')
   
]