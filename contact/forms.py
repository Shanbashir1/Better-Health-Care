from django import forms
from .models import ContactModel



# class ContactForm(forms.Form):

#         first_name = forms.CharField(max_length = 50)
#         last_name = forms.CharField(max_length = 50)
#         email = forms.EmailField(max_length = 150)
#         subject = forms.CharField(max_length = 200)
#         message = forms.CharField(widget = forms.Textarea(attrs={
#             'class': 'custom-form-field'
#             }), max_length = 2000)
#         email.required = True
#         first_name.required = True
#         last_name.required = True
#         first_name.widget.attrs.update({'class': 'custom-form-field'})
#         last_name.widget.attrs.update({'class': 'custom-form-field'})
#         email.widget.attrs.update({'class': 'custom-form-field'})
#         subject.widget.attrs.update({'class': 'custom-form-field'})

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = [ 'first_name', 'last_name', 'email', 'subject', 'message']
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