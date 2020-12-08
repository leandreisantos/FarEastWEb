from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required

import json
import datetime

from .models import *
from .forms import CreateUserForm
from .decorators import unauthenticate_user,allowed_users

# Create your views here.
total_items=0

@unauthenticate_user
def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')

            group = Group.objects.get(name='customer')
            user.groups.add(group)
            Customer.objects.create(
                 user=user,
                 name=user,
                 email=email,

            )

            messages.success(request, 'You successfuly create your account ' + username)

            return redirect('login')

    context = {'form':form}
    return render(request,'fareast/register.html',context)

@unauthenticate_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request,'Username or Password is incorrect')

    context = {'carousel':7}
    return render(request,'fareast/login.html',context)

def logoutUser(request):
    logout(request)
    return redirect('home')

@login_required(login_url='login')
def account(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()


    context = {'carousel':6, 'order':order}
    return render(request,'fareast/account.html',context)

def home(request):
    dishes = Dishes.objects.all()
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
    else:
        order = ['']

    context = {'dishes':dishes, 'order':order, 'carousel':1}
    return render(request,'fareast/home.html',context)


def menu(request):
    dishes = Dishes.objects.all()
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
    else:
        order = ['']

    context = {'dishes':dishes,'order':order,'carousel':2}
    return render(request, 'fareast/menu.html', context)

def about(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
    else:
        order = ['']
    context = {'carousel':3,'order':order}
    return render(request,'fareast/about.html',context)


def contact(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
    else:
        order = ['']
    context = {'carousel':4,'order':order}
    return render(request,'fareast/contact.html',context)


@login_required(login_url='login')
def bag(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()


    context = {'items':items, 'order':order ,'carousel':5}
    return render(request, 'fareast/bag.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['customer','admin'])
def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()

    context = {'items':items, 'order':order}

    return render(request, 'fareast/checkout.html', context)


def updateItem(request):
    data=json.loads(request.body)
    productId=data['productId']
    action=data['action']

    print('Action',action)
    print('productId',productId)

    customer=request.user.customer
    product=Dishes.objects.get(id=productId)
    order, created=Order.objects.get_or_create(customer=customer,complete=False)

    orderItem,created=OrderItem.objects.get_or_create(order=order,product=product)

    if action =='add':
        orderItem.quantity=(orderItem.quantity+1)
    elif action=='remove':
        orderItem.quantity=(orderItem.quantity-1)
    elif action == 'delete':
        orderItem.quantity=0

    orderItem.save()

    if orderItem.quantity<=0:
        orderItem.delete()

    return JsonResponse('Item was added',safe=False)


def processOrder(request):
    transaction_id=datetime.datetime.now().timestamp()
    data=json.loads(request.body)
    if request.user.is_authenticated:
        customer=request.user.customer
        order, created=Order.objects.get_or_create(customer=customer,complete=False)
    else:
        customer,order=guestOrder(request,data)

    total=float(data['form']['total'])
    order.transaction_id=transaction_id

    if total==order.get_cart_total:
        order.complete=True
    order.save()


    if order.shipping ==True:
        ShippingAddress.objects.create(
            customer=customer,
            order=order,
            address=data['shipping']['address'],
            city=data['shipping']['city'],
            state=data['shipping']['state'],
            zipcode=data['shipping']['zipcode'],
        )

    return JsonResponse('Payment complete', safe=False)
