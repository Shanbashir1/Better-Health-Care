from django.test import TestCase, Client
from django.urls import reverse


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.home_url = reverse('home')
        self.BookAppointment_url = reverse('book_appointment')
        self.ManageAppointment_url = reverse('manage-appointments')

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
