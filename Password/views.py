from django.shortcuts import render,redirect
from .models import GP
import random
import string
from django.contrib import messages
# Create your views here.

def home(request):
    p3=GP.objects.all()
    
    return render(request,'index.html',{'p1':p3})

def password(request):
    if request.method=='POST':
        p1=GP()
        try:
            length=int(request.POST['length'])
            
        except:
            messages.info(request,'please enter numbers only!')
            return redirect('/')
        else:   
             
            password_characters = string.ascii_lowercase 
            q=request.POST.get('checkbox[]')
            if q in ['string.ascii_uppercase']:
                password_characters +=string.ascii_uppercase
            elif q in ['string.digits']:
                password_characters += string.digits
            elif q in ['string.punctuation']:
                password_characters += string.punctuation   
            else:
                password_characters = string.ascii_letters + string.digits + string.punctuation
            p1.p= ''.join(random.choice(password_characters) for i in range(length))
            p1.save()
            return redirect('/')

