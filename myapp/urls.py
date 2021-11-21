
from django.urls import path
from .views import *
urlpatterns = [
    path('',index, name='index'),
    path('form/',Forms,name='form'),
    path('dropdown/',DropDownSearch,name='dropdown')
]