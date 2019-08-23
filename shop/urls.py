from django.urls import path
from . import views


urlpatterns = [
    path('', views.shop, name='shop-home'),
    path('about', views.about, name='shop-about'),
    path('pricing', views.pricing, name='shop-pricing'),
    path('contact', views.contact, name='shop-contact'),


]
