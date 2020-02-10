from django.urls import path

from votacao.views import index

urlpatterns = [
    path('', index),
    path('votar/', index),
   

   
]
