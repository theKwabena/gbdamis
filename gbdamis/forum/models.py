import os
from django.db import models
from django.conf import settings
# Create your models here.
from django.db import models
from django.contrib.auth.models import User


from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType

from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Like(models.Model):
    liked_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()


class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = RichTextUploadingField()
    date_posted = models.DateTimeField(auto_now_add=True)
    tag = models.ManyToManyField('Tag', blank = True )
    likes = GenericRelation(Like)
    featured_image = models.ImageField(upload_to='images', blank = True, default = '')

    def __str__(self):
        return self.title
    
    @property
    def get_short_title(self):
        title_len = len(self.title)
        if title_len > 35:
            return f"{self.title[0:35]}..."
        else:
            return self.title
        
    def get_forum_title(self):
        title_len = len(self.title)
        if title_len > 60:
            return f"{self.title[0:60]}..."
        else:
            return self.title


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    likes =GenericRelation(Like)


    def __str__(self):
        return f"{self.post} {self.comment}"
    

class UploadedFile(models.Model):
    uploaded_file = models.FileField(upload_to=u"storage/")
    uploaded_at = models.DateField(editable=False, auto_now_add=True)

    def __str__(self):
        return os.path.basename(self.uploaded_file.path)

    def url(self):
        return self.uploaded_file.url

    def delete(self, *args, **kwargs):
        file_storage, file_path = self.uploaded_file.storage, self.uploaded_file.path
        super(UploadedFile, self).delete(*args, **kwargs)
        file_storage.delete(file_path)
