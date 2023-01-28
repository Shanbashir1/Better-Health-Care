from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .views import Index, BookAppointment, ManageAppointment


class Test_Urls(SimpleTestCase):


    def test_home_url_is_resolved(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func.view_class, Index)

    def test_BookAppointment_url_is_resolved(self):
        url = reverse('book_appointment')
        self.assertEquals(resolve(url).func.view_class, BookAppointment)    

    def test_ManageAppointment_url_is_resolved(self):
        url = reverse('manage-appointments')
        self.assertEquals(resolve(url).func.view_class, ManageAppointment)
