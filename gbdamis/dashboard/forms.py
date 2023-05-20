from django import forms
from .models import Event, News, Announcement



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


