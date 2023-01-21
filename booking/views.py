import datetime
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from bootstrap_datepicker_plus.widgets import DateTimePickerInput
from .forms import BookAppointmentForm
from .models import BookAppointmentModel
from django.views.generic import TemplateView



class Index(generic.TemplateView):

    template_name = 'index.html'



'''
Once the booking has been created, the user will be directed to the manage booking page. 
The data recorded from the form will be displayed on the admin page.
'''
class BookAppointment(LoginRequiredMixin, CreateView):

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


'''
The Manage page will allow the user to view the booking, if the user is logged in. .
'''
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


'''
The delete page will allow the user to delete the booking, if they no longer require the appointment.
'''
class DeleteAppointment(DeleteView):

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


'''
The user will have a option to update the booking and view the updated changes. 
'''
class UpdateAppointment(LoginRequiredMixin, UpdateView):
    '''
    Handels update, if user wants to make any changes in already
    created appointment
    '''
    model = BookAppointmentModel
    template_name = 'update-appointments.html'
    form_class = BookAppointmentForm
    success_url = '/manage-appointments/'


    def get(self, request, *args, **kwargs):
        appointment = get_object_or_404(BookAppointmentModel, id=kwargs['pk'])
        if appointment.patient != request.user:
            # The users don't match
            messages.error(request, "You do not have access to manage this booking.")
            return redirect('manage-appointments')
        else:
            context = {'form': self.form_class(instance=appointment)}
            return render(request, self.template_name, context)
            
def error_404_view(request, exception):
    return render(request,'404.html')

def error_500_view(request):
    return render(request,'500.html')