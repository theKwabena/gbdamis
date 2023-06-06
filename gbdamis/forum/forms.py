from django import forms
from .models import Post,Tag,Comment
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class PostForm(forms.ModelForm):
    title = forms.CharField(widget = forms.TextInput(attrs = {
        "class": "form-control",
        "label": "Title"
    }))

    content = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Post
        fields = ['title', 'content']


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = "__all__"



