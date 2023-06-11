# import modelform from django
from django.forms import ModelForm
from django.contrib.auth import get_user_model

User = get_user_model()

class MemberUpdateForm(ModelForm):
    class Meta:
        model = User
        fields = [
            'first_name', 
            'other_names', 
            'date_of_birth', 
            'phone_number', 
            'whatsapp_number', 
            'company_name', 
            'region_or_zone',
            'field',
            'drilling_licence',
            'profession',
            'education',
            'referee',
            'referee_contact',
        ]



