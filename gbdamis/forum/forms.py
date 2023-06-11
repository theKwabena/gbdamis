from django import forms
from .models import Post,Tag,Comment
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from crispy_forms.helper import FormHelper
from django_select2 import forms as s2forms


class TagWidget(s2forms.ModelSelect2TagWidget):
    search_fields = [
        'name__icontains',
    ]
    

class PostForm(forms.ModelForm):
    title = forms.CharField(widget = forms.TextInput(attrs = {
        "class": "form-control",
        "label": "Title",
        'placeholder' : 'Enter post title here'
    })) 

    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Post
        fields = ['title', 'content', 'tag', 'featured_image']
        widgets = {
           'tag' : TagWidget
            }
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False 
    


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name']

    


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = "__all__"



