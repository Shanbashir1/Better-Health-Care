from django.contrib import admin
from .models import BookAppointmentModel
from django_summernote.admin import SummernoteModelAdmin



# @admin.register(Appointment)
# class AppointmentAdmin(SummernoteModelAdmin):

#     list_filter = ('created_on', 'doctor', 'status' )
#     summernote_fields = ('content')
#     search_fields = ('first_name', 'surname')
#     actions = ('status')

@admin.register(BookAppointmentModel)



class BookAppointmentAdmin(admin.ModelAdmin):
    '''
    The admin page, will display benefit search and actions filters for the site admin.
    '''

    list_display = ('title', 'first_name', 'last_name', 'email', 'created_on',
                      'status')
    list_filter = ('admin_decision', 'created_on')
    search_fields = ('first_name', 'surname')
    actions = ('approve_request', 'decline')

    def approve_request(self, request, queryset):

        queryset.update(status=0)

    def decline(self, request, queryset):

        queryset.update(status=0)



