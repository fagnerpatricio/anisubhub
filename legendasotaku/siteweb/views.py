from django.shortcuts import render
from django.http import HttpResponse
from .models import Series

import couchdb

def index(request):

    server = couchdb.Server('http://admin:123456@192.168.2.203:5984')
    db = server['animes']  

    urls_figuras = []
    for id in db:
        urls_figuras.append((db[id]['title'],db[id]['picture']))
    # listaDeSeries = Series.objects.filter(titulo="K-ON!") 
    # listaDeSeries = Series.objects.all()
    # for serie in listaDeSeries:
    #     print(serie.url_crunchyroll) 
    # return render(request, 'index.html',{'Series': listaDeSeries})
    return render(request, 'index.html',{ 'urls_figuras': urls_figuras })
    # return HttpResponse("Hello, world! Mundo Aberto")
