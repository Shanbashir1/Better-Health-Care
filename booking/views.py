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
        return super().form_valid(form)




    # template_name = 'book_appointment.html'
    # form_class = BookAppointmentForm

    # def form_valid(self, form):
    #     form.instance.patient = self.request.user
    #     form.save()
    #     messages.success(
    #         self.request,
    #         'Your request has been submitted and is awaiting for approval')
    #     return HttpResponseRedirect('index')