from django import forms
import datetime
from .models import Job
from django.forms.models import ModelChoiceField
from django.conf import settings


City =( 
    ("Multan", "Multan"), 
    ("Other", "Other"), 
) 

class form1(forms.Form):
	name = forms.CharField(max_length=200)
	father_name = forms.CharField(max_length=200)
	cnic = forms.CharField(max_length=200)
	phone_no = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'WhatsApp'}))
	email = forms.CharField(max_length=200)
	experience = forms.CharField(max_length=200)
	address = forms.CharField(max_length=200)
	current_city = forms.ChoiceField(choices = City)