from django.shortcuts import render
import email
from email import message
from unicodedata import name
from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

from pytest import param
from .models import Contact, Payment
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from .paytm import Checksum
from .paytm.Checksum import verify_checksum
from.models import OrderUpdate
from.models import Product,Event_Registration,EVent
MERCHANT_KEY = "bKMfNxPPf_QdZppa"
def index(request):
    context = {"variable":""}
    return render (request, 'index.html',context)
    #return HttpResponse('homepage')

def about(request):

    return render (request, 'about.html')
    #return HttpResponse('about page')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        contact = Contact(name=name,email=email,phone=phone,message=message,date=datetime.today())
        contact.save()
        messages.success(request, 'Submitted Successfully')
        





    return render (request, 'contact.html')
def productView(request, myid):

    # Fetch the product using the id
    product = Product.objects.all
    return render(request, 'prodview.html', {'product':product[0]})

def payment(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        amount = request.POST.get('amount')
        
        order = Payment(name=name,email=email,phone=phone,message=message,amount=amount,date=datetime.today())
        order.save()
        #update = OrderUpdate(order_id=order.order_id, update_desc="The order has been placed")
        #update.save()
        #thank = True
        #id = order.order_id
        messages.success(request, 'paid Successfully')
       # param_dict =  {

               # 'MID': 'DIY12386817555501617',
                #  'ORDER_ID':str(order.order_id),
               # 'TXN_AMOUNT': str(amount),
                #'CUST_ID': email,
                #'INDUSTRY_TYPE_ID': 'Retail',
                #'WEBSITE': 'WEBSTAGING',
                #'CHANNEL_ID': 'WEB',
                #'CALLBACK_URL':'http://127.0.0.1:8000/handlerequest',

        #}
        #param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(param_dict, MERCHANT_KEY)
        #return render(request, 'paytm.html', {'param_dict': param_dict})

    return render (request, 'payment.html')   
        
#@csrf_exempt
#def handlerequest(request):
    #form = request.POST
    #response_dict = {}
    for i in form.keys():
        response_dict[i] = form[i]
        if i == 'CHECKSUMHASH':
            checksum = form[i]

    verify = Checksum.verify_checksum(response_dict, MERCHANT_KEY, checksum)
    if verify:
        if response_dict['RESPCODE'] == '01':
            print('order successful')
        else:
            print('order was not successful because' + response_dict['RESPMSG'])
    return render(request, 'paymentstatus.html', {'response': response_dict})

def Event_reg(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        address = request.POST.get('address')
        event  = Event_Registration(name=name,email=email,phone=phone,message=message,address=address,date=datetime.today())
        event.save()
        messages.success(request, 'Submitted Successfully')
        





    return render (request, 'Event_Registration.html')

def eVent(request) :
    incident= EVent.objects.all()
    return render(request,'events.html',{"incident":incident})

def team(request) :
    return render (request,'team.html')
def getaway(request):
    return render (request,'getaway.html')

def online(request):
    return render (request,'online.html')
def offline (request):
    return render (request,'offline.html')    
# Create your views here.
