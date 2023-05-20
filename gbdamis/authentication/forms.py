from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import (
    UserCreationForm
)

User = get_user_model()


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "input-text"
            }
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'type': 'password',
                "placeholder": "Password",
                "class": "input-text"
            }
        ))
    
    agree =forms.BooleanField(
        required=False, 
        initial=False, 
        widget=forms.CheckboxInput())
    

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "First name",
                "class": "input-text"
            }
        ))
    
    
    other_names = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Other names",
                "class": "input-text"
            }
        ))
    
    phone_number = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Phone number",
                "class": "input-text"
            }
        ))
    
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Email",
                "class": "input-text"
            }
        ))
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "input-text"
            }
        ))
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Confirm Password",
                "class": "input-text"
            }
        ))

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2', 'first_name', 'other_names', 'phone_number')
        
        
    def clean_email(self):
       email = self.cleaned_data.get('email')
       if User.objects.filter(email=email).exists():
            raise ValidationError("An account with this email address exists")
       return email
    
    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if User.objects.filter(phone_number=phone_number).exists():
                raise ValidationError("An account with this phone number exists")
        return phone_number

    
    
