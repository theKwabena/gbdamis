# Create a class to handle all paystack related functions
# The class should import the paystack secret key from project settings
# The constructor should initialize the paystack secret key and set it as an instance variable
# The class should set the headers for the paystack api using the secret key
import json
import requests


class Paystack:
    def __init__(self):
        self.base_url = 'https://api.paystack.co'
        self.secret_key = settin
        self.headers = dict(Authorization=f'Bearer {self.secret_key}', Content_Type='application/json')


class Charge(Paystack):
    def __init__(self):
        Paystack.__init__(self) 
        self.charge_url = f'{self.base_url}/charge'
        self.reference = None
        self.contact = dict(number=None, provider=None)
        self.amount = None
        self.member = None

    def get_provider(self, number=None):
        if number:
            self.contact.number = number
        
        mtn = ['024', '054', '055']
        vodafone = ['020', '050']
        airteltigo = ['027', '057']
        if self.contact.number.startswith(tuple(mtn)):
            self.phone.provider = 'MTN'
            return self.phone.provider
        elif self.contact.number.startswith(tuple(vodafone)):
            self.phone.provider = 'vod'
            return self.phone.provider
        elif self.contact.number.startswith(tuple(airteltigo)):
            self.phone.provider = 'tgo'
            return self.phone.provider
        else :
            return None

    def request_charge(self,number=None):
        data = json.dumps(dict(
            amount=self.amount,
            email=self.member.email,
            currency = 'GHS',
            mobile_money = dict(
                phone = number if number else self.contact.number,
                provider = self.get_provider(number if number else None)
            )
        ))
        response = requests.post(self.charge_url, data=data, headers=self.headers)
        if response.status_code == 200:
            self.reference = response.json()['data']['reference']
            return response.json()
        else:
            return None
        
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
            return None
