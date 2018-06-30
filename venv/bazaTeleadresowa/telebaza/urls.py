from django.urls import path
from django.conf.urls import url
from django.conf import settings
from . import views

app_name = 'telebaza'

urlpatterns = [
    path('', views.printMsg, name='printMsg'),
    path('listPeople/', views.listPeople, name='listPeople'),
    path('addPerson/', views.addPerson, name='addPerson'),

]