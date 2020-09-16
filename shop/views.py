from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

from .models import *


def index(request):
    return render(request, "index.html")


def about_us(request):
    return render(request, "about.html")


def menu(request):
    return render(request, "menu.html")

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