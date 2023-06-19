from django.conf import settings
from django.contrib.admin.views.decorators import staff_member_required
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_exempt
from ckeditor_uploader.views import upload, browse
from gbdamis.forum.models import UploadedFile
import re

@staff_member_required
@csrf_exempt
def ckeditor_upload_wrapper(request, *args, **kwargs):
    response = upload(request, *args, **kwargs)

    if b"Invalid" not in response.content:
        try:
            matched_regex = re.search("callFunction\(\d, '(.*)'\);", str(response.content))
            file_location = matched_regex.group(1).lstrip(settings.MEDIA_URL)
            UploadedFile(uploaded_file=file_location).save()
        except Exception:
            pass
    return response

@staff_member_required
@csrf_exempt
@never_cache
def ckeditor_browse_wrapper(request, *args, **kwargs):
    return browse(request, *args, **kwargs)