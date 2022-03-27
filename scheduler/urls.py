
from django import views
from django.contrib import admin
from django.urls import path
from .views import index,upload,show_data
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', upload,name='upload'),
    path('graph',index,name='home'),
    path('success',show_data,name='success'),
]
