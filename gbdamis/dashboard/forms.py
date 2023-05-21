from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError


from crispy_forms.helper import FormHelper

from .models import Event, News, Announcement


User = get_user_model()

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields ="__all__"


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = "__all__"


class AnnouncementForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = "__all__"


class AddMemberForm(forms.Form):
    
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "First name",
                'id' : 'firstname'
            }
        ))
    
    
    other_names = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Other names",
                'id': 'othernames'
            }
        ))
    
    phone_number = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Phone number",
                'id' : 'phone_number',
                'type' : 'tel'
            }
        ))
    
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Email",
                "class": "input-text",
                'id' : 'email'
            }
        ))
    
    def __init__(self, *args, **kwargs):
        super(AddMemberForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False 

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


   