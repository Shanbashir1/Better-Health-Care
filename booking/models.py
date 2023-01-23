from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# Choices created for users to be displayed options 

STATUS = ((0, 'Waiting_Approval'), (1, 'Approved'), (2, 'Decline'))
TITLE_STATUS = (('MR', 'Mr'),('MRS', 'Mrs'),('MS', 'Ms'),('MISS', 'Miss'))
DR_NAME = (('DR KEEN', 'Dr Keen'),('DR PATEL', 'Dr Patel'),('DR REUBIN', 'Dr Reubin'),('DR WATSON', 'Dr Watson'))
URGENCY = (('NOT URGENT', 'Not Urgent'), ('URGENT', 'Urgent'))



class BookAppointmentModel(models.Model):
    '''
    The BookAppointmentModel allows the admin to receive information
    relating to the patients, and created files and data for the
    patients. .
    '''

    title = models.CharField(max_length=4, choices=TITLE_STATUS)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    patient = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user_booking', null=True)
    nhs_number = models.CharField(max_length=10, null=True)
    email = models.EmailField(max_length=40)
    created_date = models.DateField(null=True)
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)
    message = models.TextField(null=True)
    urgent = models.CharField(max_length=10, choices=URGENCY, null=True)
    status = models.IntegerField(choices=STATUS, default=0)
    doctor = models.CharField(max_length=20, choices=DR_NAME)
    admin_decision = models.BooleanField(default=False)
    

    class Meta:
        ordering = ['-created_date']
        verbose_name = ("Book Appointment Model")

    def __str__(self):
        return str (self.first_name)
