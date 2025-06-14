from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.Home,name="Home"),
    path('aboutus/',views.Aboutus,name='aboutus'),
    path('contactus/',views.Contactus,name='contactus'),
    path('social_media/',views.SocialMedia,name='social_media'),
    path('web_dev/',views.Web_dev,name='web_dev'),
    path('creative_design/',views.CreativeDesign,name='creative_design'),
    path('services/',views.Services,name='services'),
]