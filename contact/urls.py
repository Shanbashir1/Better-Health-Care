
'''
Contact urls
'''
from django.urls import path, include
from . import views



urlpatterns = [
    path('contact/', views.ContactUs.as_view(), name='contact'),
    path('about', views.About.as_view(), name="about"),
]