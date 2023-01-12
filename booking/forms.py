import datetime
from django import forms
from .models import BookAppointmentModel
from bootstrap_datepicker_plus.widgets import DatePickerInput, TimePickerInput, DateTimePickerInput, MonthPickerInput, YearPickerInput


CURRENT_DATE = str(datetime.date.today())


class BookAppointmentForm(forms.ModelForm):
    '''
    Handles book appointment form.
    The Bootstrap datepicker library was installed, which makes
    form looks more appealing
    '''

    class Meta:
        model = BookAppointmentModel
        fields = ('title', 'first_name', 'last_name', 'nhs_number', 'email', 'created_date', 'doctor', 'message', 'urgent',)

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

                                        
        