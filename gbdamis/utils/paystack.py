# Create a class to handle all paystack related functions
# The class should import the paystack secret key from project settings
# The constructor should initialize the paystack secret key and set it as an instance variable
# The class should set the headers for the paystack api using the secret key
import json
from django.conf import settings
import requests


class Paystack:
    def __init__(self):
        self.base_url = 'https://api.paystack.co'
        self.secret_key = getattr(settings, 'PAYSTACK_SECRET_KEY', None)
        self.headers = dict(Authorization=f'Bearer {self.secret_key}', Content_Type='application/json')


class Charge(Paystack):
    def __init__(self, member, amount,contact=None):
        Paystack.__init__(self) 
        self.charge_url = f'{self.base_url}/charge'
        self.reference = None
        self.contact = dict(phone_number=contact, provider=None)
        self.amount = amount
        self.member = member

    def get_provider(self): 
        mtn = ['024', '054', '055']
        vodafone = ['020', '050']
        airteltigo = ['027', '057']
        if self.contact.phone_number.startswith(tuple(mtn)):
            self.contact.provider = 'MTN'
            return self.phone.provider
        elif self.contact.phone_number.startswith(tuple(vodafone)):
            self.contact.provider = 'vod'
            return self.phone.provider
        elif self.contact.phone_number.startswith(tuple(airteltigo)):
            self.contact.provider = 'tgo'
            return self.phone.provider
        else :
            return None

    def request_charge(self, momo_number=None):
        if momo_number:
            self.contact.phone_number = momo_number
        data = json.dumps(dict(
            amount=self.amount,
            email=self.member.email,
            metadata=dict(
                member_id=self.member.id,
                member_first_name=self.member.first_name,
                member_other_names=self.member.other_names,
                member_email=self.member.email,
                member_phone=self.member.phone_number,
            ),
            currency = 'GHS',
            mobile_money = dict(
                phone =  self.contact.phone_number,
                provider = self.get_provider()
            )
        ))
        response = requests.post(self.charge_url, data=data, headers=self.headers)
        if response.status_code == 200:
            self.reference = response.json()['data']['reference']
            success = dict(
                status = True,
                status_code = response.status_code,
                data = response.json()
            )
            return success
        else:
            error = dict(
                status = False,
                status_code = response.status_code,
                data = response.json()
            )
            return error
        
    def verify_otp(self, otp):
        verify_url = f'{self.base_url}/charge/submit_otp'
        data = json.dumps(dict(
            otp=otp,
            reference=self.reference
        ))
        response = requests.post(verify_url, data=data, headers=self.headers)
        if response.status_code == 200:
            return response.json()
        else:
            error = dict(
                error_code = response.status_code,
                data = response.json()
            )
            return error
        
    def verify_payment(self):
        verify_url = f'{self.base_url}/charge/verify'
        data = json.dumps(dict(
            reference=self.reference
        ))
        response = requests.post(verify_url, data=data, headers=self.headers)
        if response.status_code == 200:
            return response.json()
        else:
            error = dict(
                error_code = response.status_code,
                data = response.json()
            )
            return error
