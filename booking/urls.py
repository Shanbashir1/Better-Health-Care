from django.urls import path
from .views import Index, BookAppointment

urlpatterns = [
    path('', Index.as_view(), name='home'),
    path('book_appointment/', BookAppointment.as_view(),
         name='book_appointment'),
]
