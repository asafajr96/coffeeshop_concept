from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

from .models import Product


def index(request):
    return render(request, "index.html")


def about_us(request):
    return render(request, "about.html")


def menu(request):
    return render(request, "menu.html")

@csrf_exempt
def shop(request):
    product_list = Product.objects.all()

    context = {"product_list":product_list}
    return render(request, "store/shop.html", context)


def cart(request):
    context = {}
    return render(request, "store/cart.html", context)


def checkout(request):
    context = {}
    return render(request, "store/checkout.html", context)