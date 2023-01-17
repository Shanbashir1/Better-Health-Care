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
    Created a custom admin page to simplify admin tasks
    and give admins more control over the users.
    '''
    list_display = ('title', 'first_name', 'last_name', 'email', 'created_on',
                      'status')
    list_filter = ('admin_decision', 'created_on')
    search_fields = ['name']
    actions = ['approve_request', 'not_approved']

    def approve_request(self, request, queryset):
        '''
        Handels status choices
        '''
        queryset.update(status=0)



