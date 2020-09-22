from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from .models import *
from .forms import ContactForm
from django.contrib import messages


def index(request):
    return render(request, "index.html")


def about_us(request):
    return render(request, "about.html")

@csrf_exempt
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        
        if form.is_valid():
            
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            email = form.cleaned_data['email']

            recipients = ['vminimaldesign@gmail.com']

            send_mail(subject, message, email, recipients, fail_silently=False)
            
            messages.success(request, "Email was sent successfully.")

            return redirect("contact_page")
        
    form = ContactForm()
    context = {'form': form}
    return render(request, 'contact.html', context)



@csrf_exempt
def shop(request):
    product_list = Product.objects.all()

    context = {"product_list":product_list,}
    return render(request, "store/shop.html", context)


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {"get_carttotal":0, "get_cart_items":0}
    context = {"items":items, "order":order}
    return render(request, "store/cart.html", context)


def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {"get_carttotal":0, "get_cart_items":0}
    context = {"items":items, "order":order}
    return render(request, "store/checkout.html", context)