from django.urls import path
from .views import *

urlpatterns=[
    path("add/<int:id>",addtocart),
    path('view',viewcart),
    path('remove/<int:pid>',removefromcart),
    path('update',update),
    # path('summery',summery),
    # path('savedata',save)
]



