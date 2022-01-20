from django.urls import path, include
from .views import *



urlpatterns = [
    path('', index, name='main_page'),
    path('profile', profile, name='profile_page'),
    path('test_study', test_study, name='test_study_page'),
]
