from django.contrib import messages
from django.views.generic.edit import FormView
from django.http import HttpResponseRedirect
from .forms import ContactForm


class ContactUs(FormView):
    '''
    Sends back a message to users who fill out a contact form
    '''
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = '/contact/'

def my_view(request):
       if form.is_valid():
          messages.success(request, 'Form submission successful')
