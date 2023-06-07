from django import forms
from .models import Post,Tag,Comment
from ckeditor_uploader.widgets import CKEditorUploadingWidget


from django_select2 import forms as s2forms


class TagWidget(s2forms.ModelSelect2Widget):
    search_fields = [
        "name__icontains",
        
    ]


class PostForm(forms.ModelForm):
    title = forms.CharField(widget = forms.TextInput(attrs = {
        "class": "form-control",
        "label": "Title"
    })) 

    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Post
        fields = ['title', 'content', 'tag']
        widgets = {
           'tag' : s2forms.Select2TagWidget
            }
    


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = "__all__"



