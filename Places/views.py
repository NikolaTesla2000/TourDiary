from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse
from .models import Description
from .models import Contact
# Create your views here.
def welcome(request):
       return render(request, 'welcome.html')
def index(request):    # Our index page
       descriptions= Description.objects.all
       return render(request, 'index.html', {'description': descriptions})
def Images(request,value):
       imgs= Description.objects.get(id=value)
       return render(request,'images.html',{'img':imgs})
def contact(request):
       if request.method=="POST":
              fname = request.POST.get('fname')
              lname = request.POST.get('lname')
              email = request.POST.get('email')
              phone = request.POST.get('phone')
              desc = request.POST.get('desc')
              contact=Contact(fname=fname,lname=lname,email=email,phone=phone,desc=desc,date=datetime.today())
              contact.save()

       return render(request,'contact.html')