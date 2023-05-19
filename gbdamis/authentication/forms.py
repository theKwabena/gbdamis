from django import forms



class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "input-text"
            }
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "input-text"
            }
        ))
    
    agree =forms.BooleanField(
        required=False, 
        initial=False, 
        widget=forms.CheckboxInput())