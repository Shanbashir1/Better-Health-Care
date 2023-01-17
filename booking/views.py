'''
Booking_app Views
'''
import datetime
from django.views import generic
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from bootstrap_datepicker_plus.widgets import DateTimePickerInput
from .forms import BookAppointmentForm
from .models import BookAppointmentModel



class Index(generic.TemplateView):
    '''
    Hisplay home view for the site
    '''
    template_name = 'index.html'



class BookAppointment(CreateView):
    '''
    After submitting the form user details will be saved in the database
    and users will be redirected to the manage booking page.
    '''
    form_class = BookAppointmentForm
    template_name = 'book_appointment.html'
    success_url = reverse_lazy('book_appointment')

    '''
    Sends the data back to the admin page 
    '''
    def form_valid(self, form):
        form.instance.patient = self.request.user
        messages.success(
        self.request,
        "Thank you for your booking request, your booking \
            has been forwarded onto our booking team \
            if your appointment has been approved, you will be \
                notified via our manage booking page.")
        form.save()
        return HttpResponseRedirect('/manage-appointments/')

class ManageAppointment(generic.ListView):

    model = BookAppointmentModel
    template_name = 'manage-appointments.html'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['appointments'] = context['object_list']
        return context

    def get_queryset(self):
        return BookAppointmentModel.objects.filter(
            patient=self.request.user).order_by("created_date")

class DeleteAppointment(DeleteView):
    '''
    Handles the delete option for users, letting them
    cancel their appointment if they wish.
    '''
    model = BookAppointmentModel
    success_url = '/manage-appointments/'
    template_name = "delete-appointments.html"

    def deleted_appointment(self, request, pk, *args, **kwargs):
        '''
        methods handels delete
        '''
        appointments = BookAppointmentModel.objects.get(
            pk=self.request.pk)
        appointments.delete()

class UpdateAppointment(UpdateView):
    '''
    Handels update, if user wants to make any changes in already
    created appointment
    '''
    model = BookAppointmentModel
    template_name = 'update-appointments.html'
    form_class = BookAppointmentForm
    success_url = '/manage-appointments/'
