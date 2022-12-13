from django.urls import path
from .views import *

urlpatterns=[
    path('saveadd/',saveadd),
    path('place',placeorder),
    path('invoice',invoice)
]