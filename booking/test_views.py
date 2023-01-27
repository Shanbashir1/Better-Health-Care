from django.test import TestCase
from .models import BookAppointmentModel

class TestViews(TestCase):

    def test_get_home(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_get_about(self):
        response = self.client.get("/about")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')

    def test_get_contact(self):
        response = self.client.get("/contact")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')

    def test_get_booking_appointment(self):
        response = self.client.get("/booking_appointment")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')

    def test_get_manage_appointment(self):
        response = self.client.get("/manage_appointments")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')

    def test_get_delete_appointment(self):
        response = self.client.get("/delete_appointments")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')

    def test_get_update_appointment(self):
        response = self.client.get("/update_appointments")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')

    def test_get_404_page(self):
        response = self.client.get("/404")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')
