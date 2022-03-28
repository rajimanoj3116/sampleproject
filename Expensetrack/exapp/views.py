from django.forms.forms import Form
from django.http import request
from django.shortcuts import redirect, render
from django.utils import html
from exapp.forms import UserRegistrationForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from exapp.forms import ExpenseForm
from exapp.forms import exform
from exapp.forms import balanceform
from exapp.forms import BalanceForm
from exapp.models import Balance, Expense
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,'index.html')

def signin(request):
    if request.method=='POST':
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'signup sccessfully')
            return redirect('index')
    form=UserRegistrationForm()
    return render(request,'signin.html',{'form':form})
def Login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            form=login(request,user)
            messages.success(request,'login successfully')
            return redirect('home')  
        else:
            messages.info(request,'user doesnot exist') 

    form=AuthenticationForm()
    return render(request,'login.html',{'form':form})                     
def home(request):
    form1=exform()
    sr=ExpenseForm()
    st=balanceform()
    form=BalanceForm()
    details=Expense.objects.all()
    return render(request,'home.html',{'sr':sr,'form1':form1,'form':form,'st':st,'details':details}) 


def balance(request):
    
    form=balanceform()
    st=BalanceForm()
    balance=request.POST['balance']
    if st.is_valid():
        res="balance updated successfully"
        details=Balance.objects.all()
        details.save()
        return HttpResponse(request,'home.html',{'form':form,'st':st,'details':details,'res':res})      
      

def addexpense(request):
  form=exform()
  se=ExpenseForm()
  st=BalanceForm()
  
  details=Expense.objects.all()
  bvalue=Balance.objects.all()
  if details > bvalue:
      res="balance not exist"
      return render(request,'home.html',{'form':form,'se':se,'st':st,'details':details,'bvalue':bvalue,'res':res})
  elif details.is_valid():
      res="expense updated"
      details.save()
      return render(request,'home.html',{'se':se,'st':st,'details':details,'bvalue':bvalue,'res':res})

       