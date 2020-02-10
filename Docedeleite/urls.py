from django.urls import path

from Docedeleite.views import index, doce, docegoiaba, aindatemdoce, equipe

urlpatterns = [
    path('', index),
    path('novo-doce/', doce),
    path('leite-com-goiaba/', docegoiaba),
    path('ainda-tem-doce/', aindatemdoce),
    path('equipe/', equipe),




   
]
