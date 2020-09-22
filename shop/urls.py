from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name = "home_page"),
    path('about_us/', views.about_us, name = "about_us_page"),
    path('shop/', views.shop, name = "shop_page"),
    path('cart/', views.cart, name = "cart_page"),
    path('checkout/', views.checkout, name = "checkout_page"),
    path('contact/', views.contact, name = "contact_page"),
]