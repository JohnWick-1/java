from .views import *
from django.urls import path

urlpatterns = [path('home/', show, name='index'),
               path('save/', save, name='saveStud'),
               path('showForm/', showForm, name='showform'),
               path('saveForm/', saveForm, name='saveform'),
               ]

