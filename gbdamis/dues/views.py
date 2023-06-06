import requests, json, logging
from django.shortcuts import render
from django.http import JsonResponse

from gbdamis.utils.paystack import Charge

log = logging.getLogger(__name__)


# Create your views here.

def pay_current_dues(request):
    member = request.user
    
    payment = Charge(member=member, amount=member.get_current_due.amount)
    if request.method == 'POST':
        phone_number = request.POST.get('phone_number', None)
        otp = request.POST.get('otp', None)
        if phone_number:
            log.warning(phone_number)
            pay = payment.request_charge(momo_number=phone_number)
            if pay['status']:
                return JsonResponse(pay['data'])
            else:
                return JsonResponse(pay['data'])