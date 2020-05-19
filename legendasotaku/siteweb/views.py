from django.shortcuts import render
from django.http import HttpResponse
from .models import Series

def index(request):

    # listaDeSeries = Series.objects.filter(titulo="K-ON!") 
    listaDeSeries = Series.objects.all()
    for serie in listaDeSeries:
        print(serie.url_crunchyroll) 
    return render(request, 'index.html',{'Series': listaDeSeries})
    # return HttpResponse("Hello, world! Mundo Aberto")
