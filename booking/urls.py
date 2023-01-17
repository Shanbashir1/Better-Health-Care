from django.urls import path
from .views import Index, BookAppointment, ManageAppointment, DeleteAppointment,  UpdateAppointment

urlpatterns = [
    path('', Index.as_view(), name='home'),
    path('book_appointment/', BookAppointment.as_view(),
         name='book_appointment'),
    path('manage-appointments/', ManageAppointment.as_view(),
         name='manage-appointments'), 
    path('delete-appointments/<int:pk>', DeleteAppointment.as_view(),
         name='delete-appointments'),
    path('update-appointments/<int:pk>', UpdateAppointment.as_view(),
         name='update-appointments')
]
