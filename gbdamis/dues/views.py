import requests, json, logging
from django.shortcuts import render
from django.http import JsonResponse

from gbdamis.dashboard.utils import is_ajax

from gbdamis.utils.paystack import Charge

from gbdamis.dues.models import Dues

log = logging.getLogger(__name__)


# Create your views here.

def pay_current_dues(request):
    member = request.user

    
    if request.method == 'POST':
        payment = Charge(member=member, amount=request.POST.get('amount'))
        # due = Dues.object.filter(month=month, amount=20)
        phone_number = request.POST.get('phone_number', None)
        otp = request.POST.get('otp', None)
        payment_id = request.POST.get('reference', None)
        if phone_number:
            log.warning(phone_number)
            pay = payment.request_charge(momo_number=phone_number)
            if pay['status']:
                return JsonResponse(pay['data'])
            else:
                return JsonResponse(pay['data'])
        elif otp:
            log.warning(otp)
            pay_dues = payment.verify_otp(otp)
            return JsonResponse(pay_dues['data'])
        else:
            verify_payment = payment.verify_payment(payment_id)
            if verify_payment['status']:
                due = Dues.object.get(user=request.user, id=request.POST.get('dues_id'))
                due.mark_as_paid()
                return JsonResponse(verify_payment['data'])
            else:
                return JsonResponse(verify_payment['datas'])

            
        
        


          
