import imp
from django.conf import settings
from django.urls import path
from .views import *
from django.conf.urls.static import static


urlpatterns=[
    path('index/',index),
    path('delete/<int:id>',delete),
    path('save',save),
    path('edit/<int:id>',edit),
    path('update',update),
    
   
    ]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)