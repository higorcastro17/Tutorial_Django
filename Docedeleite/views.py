from django.http import HttpResponse



def index(request):
    return HttpResponse("Hello i'm doce de leite.")

def doce(request):
    return HttpResponse("Hello Andreza, i'm  new doce de leite")

def docegoiaba(request):
    return HttpResponse("Hello new doce leite com goiaba")

def aindatemdoce(request):
    return HttpResponse("Hello have doce")

def equipe(request):
    return HttpResponse("Andreza<br>Higor</br>Laysla")
    


