from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db.models import fields
from exapp.models import Balance
from exapp.models import Expense


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','email','password1','password2']

class exform(forms.Form):
  expensename=forms.CharField(max_length=500,label="Enter Expense :")   
  amount=forms.IntegerField(label="Enter  Amount:")  

class ExpenseForm(forms.ModelForm):
   class Meta:
     model=Expense
     fields="__all__"

class balanceform(forms.Form):
  Ebalnce=forms.IntegerField(label="Enter Balance Amount:") 

class BalanceForm(forms.ModelForm):
    class Meta:
        model=Balance
        fields="__all__"  