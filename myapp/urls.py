from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about.html', views.about, name="about"),
    path('contact.html', views.contact, name="contact"),
    path('packages.html', views.packages, name="packages"),
    path('pricing.html', views.pricing, name="pricing"),
]
