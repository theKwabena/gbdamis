import requests, json, logging
from django.shortcuts import render
from django.http import JsonResponse

log = logging.getLogger(__name__)
# Create your views here.

def pay_dues(request):
    log.info(request.user)
    
    return JsonResponse({'message' : "True"})


