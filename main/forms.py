from django import forms
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError

from .models import UserRequest


class CustomEmailField(forms.EmailField):
    def __init__(self, *args, **kwargs):
        email_validator = RegexValidator(
            regex=r'@(gmail\.com|yahoo\.com|google\.com|apple\.com)$',
            message='Enter a valid email with @gmail.com, @yahoo.com, @google.com, or @apple.com domain.'
        )
        super().__init__(
            validators=[email_validator],
            *args,
            **kwargs
        )


class UserForm(forms.ModelForm):
    email = CustomEmailField()

    class Meta:
        model = UserRequest
        fields = ['name', 'email', 'phone_number', 'text']
