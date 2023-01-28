from django import forms
from .models import ContactModel


class ContactForm(forms.ModelForm):
    """
    Contact Form allows the user to enter information regarding Feedback,
    the information will be returned back to the model and admin
    """
    class Meta:
        model = ContactModel
        fields = ['first_name', 'last_name', 'email', 'subject', 'message']
        widgets = {
            'first_name': forms.TextInput(attrs={
                'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={
                'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Email'}),
            'subject': forms.TextInput(attrs={
                'placeholder': 'Subject',
            }),
        }

    def object(self):
        pass
