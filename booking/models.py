from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


STATUS = ((0, 'Waiting_Approval'), (1, 'Approved'))
TITLE_STATUS = (('MR', 'Mr.'),('MRS', 'Mrs.'),('MS', 'Ms.'),('MISS', 'Miss.'))
DR_NAME = (('DR KEEN', 'Dr Keen.'),('DR PATEL', 'Dr Patel.'),('DR REUBIN', 'Dr Reubin.'),('DR WATSON', 'Dr Watson.'))
URGENCY = (('NOT URGENT', 'Not Urgent'), ('URGENT', 'Urgent'))

# Appointment Model for user to book his/her details into the system

class Appointment(models.Model):

    title = models.CharField(max_length=4, choices=TITLE_STATUS)
    first_name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    patient_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_booking', null=True)
    email = models.EmailField(max_length=40)
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    status = models.IntegerField(choices=STATUS, default=0)
    doctor = models.CharField(max_length=20, choices=DR_NAME)
    

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
