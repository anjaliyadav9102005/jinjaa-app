from django.urls import path
from addtocart import views 

urlpatterns = [
    path('' , views.addtocart),
]
