import datetime
from django import forms
from .models import BookAppointmentModel
from bootstrap_datepicker_plus.widgets import DatePickerInput, \
    TimePickerInput, DateTimePickerInput, MonthPickerInput, YearPickerInput


CURRENT_DATE = str(datetime.date.today())


class BookAppointmentForm(forms.ModelForm):
    '''
    The BookAppointmentForm allows the users to enter data
    into the fields resulting information being
    transfered to the admin model.
    '''

    class Meta:
        '''
        The Fields will be displayed on the booking appointment page
        for the user to enter his information.
        '''
        model = BookAppointmentModel
        fields = ('title', 'first_name', 'last_name', 'nhs_number', 'email', \
                  'created_date', 'doctor', 'message', 'urgent',)

        labels = {
            'created_date': 'Request Date',
            'your_request': 'Message'
        }

        widgets = {
            'created_date': DatePickerInput(
                options={
                    "format": "DD/MM/YYYY",
                    "showClose": True,
                    "showClear": True,
                    "showTodayButton": True,
                    'minDate': CURRENT_DATE,
                }
            ),
        }


class Updateform(BookAppointmentForm):
    '''
    This will restrict the user to change certain fields
    The code was added to keep the form similar to the original booking
    rather than allow the user to change all the fields and make the booking
    seem like new.
    '''

    first_name = forms.CharField(disabled=True)
    last_name = forms.CharField(disabled=True)
    nhs_number = forms.CharField(disabled=True)
    doctor = forms.CharField(disabled=True)
    title = forms.CharField(disabled=True)
    email = forms.CharField(disabled=True)
