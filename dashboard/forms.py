from django import forms
from django.forms import models
from .models import Chamber, Dispatch, Inward
from .models import Client,Dispatch 
#from .models import Invoice, Order

class InwardForm(forms.ModelForm):
    class Meta:
        model = Inward
        field = ['name', 'category', 'quantity',]
        exclude = ['']

class ClientForm(forms.ModelForm): 
    class Meta:
        model = Client
        fields = ['name', 'email' ]
        exclude = ['']

class DispatchForm(forms.ModelForm):
    class Meta:
        model = Dispatch
        field = ['inward','product_quantity',]
        exclude = ['']

class ChamberForm(forms.ModelForm):
    class Meta:
        model = Dispatch
        field = ['inward','product_quantity']
        exclude = ['']


