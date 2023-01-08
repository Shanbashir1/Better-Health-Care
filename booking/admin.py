from django.contrib import admin
from .models import Appointment
from django_summernote.admin import SummernoteModelAdmin



@admin.register(Appointment)
class AppointmentAdmin(SummernoteModelAdmin):

    list_filter = ('created_on', 'doctor', 'status' )
    summernote_fields = ('content')
    search_fields = ('first_name', 'surname')
    actions = ('status')



