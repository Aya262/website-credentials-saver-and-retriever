from django import forms
from .models import CustomUser ,websites
from django.forms import ModelForm

class CustomCreationForm(ModelForm):
    class Meta:
        model=CustomUser
        fields=['id','email','name','secondEmail','password','phone','secondPhone','address','question','answer']

class CustomChangeForm(ModelForm):
    class Meta:
        model=CustomUser
        fields=['email','name','secondEmail','password','phone','secondPhone','address','question','answer']


class WebsiteForm(ModelForm):
    class Meta:
        model=websites
        fields=['userID','name','username','password','email','recoveremail','phone']



class ContactForm(forms.Form):
    firstname=forms.CharField(max_length=50)
    secondname=forms.CharField(max_length=50)
    subject=forms.CharField(max_length=50)
    from_email=forms.EmailField(max_length=50)
    body=forms.CharField(widget=forms.Textarea,max_length=2000)

