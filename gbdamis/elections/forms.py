from django import forms
from django.contrib.auth import get_user_model
from . models import Position, Nomination


User = get_user_model()
class PositionForm(forms.ModelForm):
    class Meta:
        model = Position
        fields = ['name',]

class NominationForm(forms.ModelForm):
    class Meta:
        model = Nomination
        fields = ['nominee', 'position']
    

    def __init__(self, *args, **kwargs):
        super(NominationForm, self).__init__(*args, **kwargs)
        self.fields['nominee'].empty_label = 'Please select nominee'
        self.fields['nominee'].label_from_instance= lambda obj: '%s - %s' % (obj.username, obj.get_full_name())

    def clean_nominee(self):
        nominee = self.cleaned_data.get('nominee')
        if nominee and Nomination.objects.filter(nominee
        =nominee).exists():
            raise forms.ValidationError('Nominee has already been nominated')
        return nominee
