from django import forms
from .models import *
from django.contrib.auth.models import User
from django.forms import ModelForm
from registration.forms import RegistrationForm
from crispy_forms.helper import FormHelper


class RegisterForm(RegistrationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        
    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
        self.helper.form_show_labels = True 

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
        widgets = {
          'bio': forms.Textarea(attrs={'rows':8, 'cols':10,}),
        }
        