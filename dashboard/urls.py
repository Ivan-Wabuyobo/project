from django.urls import path
from .views import *

urlpatterns = [
     path('', HomeView.as_view(), name="home"),
     path('about/', AboutPageView.as_view(), name="about"),
]
