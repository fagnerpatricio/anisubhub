from __future__ import unicode_literals
import json
import requests
import xml.etree.ElementTree as ET
from djongo import models

url_imgs = 'https://cdn-eu.anidb.net/images/main/'

# class SeriesManager(models.Manager):
#     def create_series(self, titulo,temporada):
#         serie = self.create(titulo=titulo,temporada=temporada)
#         anime_info = (ET.parse('/home/fagner/ProjetosVSCode/anisubhub/legendasotaku/siteweb/templates/oreimo.xml')).getroot()        
#         serie.cod_img = cod_anidb_img = '221835.jpg'
#         open('/home/fagner/ProjetosVSCode/anisubhub/legendasotaku/siteweb/templates/img/' + cod_anidb_img, 'wb').write((requests.get(url_imgs + cod_anidb_img , allow_redirects=True).content))
#         for episodio in anime_info.iter("episode"):
#             for titulo in episodio.findall('title'):
#                 if titulo.attrib['{http://www.w3.org/XML/1998/namespace}lang'] == 'en':
#                     try:
#                         serie.lista_episodes += ('#' + str(int(episodio.find("epno").text)) + ' - ' + titulo.text + '\n') 
#                     except:
#                         continue
        
#         return serie

class Series(models.Model):
    created_at = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False,auto_now=True)

    titulo = models.CharField(max_length=500,null=True)
    temporada = models.IntegerField(default=1,null=True)
    # temporada = models.IntegerField(default=1,null=True)
    #cod_tv_maze = models.CharField(max_length = 10, null=True)
    #url_tv_maze = models.URLField(max_length = 500, blank=True)
    #url_the_movie_db = models.URLField(max_length = 500, blank=True)
    #url_imdb = models.URLField(max_length = 500, blank=True)    
    cod_img = models.CharField(max_length = 50, blank=True)    
    lista_episodes = models.TextField(blank=True)
    #url_trakt = models.URLField(max_length = 500, blank=True)
    #url_crunchyroll = models.URLField(max_length = 500, blank=True)
    #url_anidb = models.URLField(max_length = 500, blank=True)
    #url_my_anime_list = models.URLField(max_length = 500, blank=True)
    # objects = SeriesManager()

    # arquivo_banner = models.ImageField(upload_to='legendasotaku/siteweb/templates/img/banners')
    #arquivo_do_banner = models.FilePathField(max_length=500, blank=False)

    def save(self, *args, **kwargs):
        #Codigo Para teste
        # file = open('/home/fagner/ProjetosVSCode/anisubhub/legendasotaku/siteweb/templates/anime.json','r')        
        # legendas = json.load(file)
        if self.pk:
            super(Series, self).save(*args, **kwargs)
        else:
            anime_info = (ET.parse('/home/fagner/ProjetosVSCode/anisubhub/legendasotaku/siteweb/templates/oreimo.xml')).getroot()
            ##################
            cod_anidb_img = '221835.jpg'
            open('/home/fagner/ProjetosVSCode/anisubhub/legendasotaku/siteweb/templates/img/' + cod_anidb_img, 'wb').write((requests.get(url_imgs + cod_anidb_img , allow_redirects=True).content))
            for episodio in anime_info.iter("episode"):
                for titulo in episodio.findall('title'):
                    if titulo.attrib['{http://www.w3.org/XML/1998/namespace}lang'] == 'en':
                        try:
                            self.lista_episodes += ('#' + str(int(episodio.find("epno").text)) + ' - ' + titulo.text + '\n') 
                        except:
                            continue
            # info = requests.get('http://api.tvmaze.com/shows/' + self.cod_tv_maze + '?embed=episodes', verify=True).json()
            # self.url_tv_maze = 'http://api.tvmaze.com/shows/' + self.cod_tv_maze
            # self.url_imdb = 'https://www.imdb.com/title/' + str(info['externals']['imdb']) + '/'
            # self.url_the_movie_db = 'https://www.themoviedb.org/tv/' + str(info['externals']['thetvdb'])
            self.cod_img = cod_anidb_img
            super(Series, self).save(*args, **kwargs) 
        

    def __str__(self):
        return (self.titulo + " -- (" + str(self.temporada) + "º Temporada)")
        # return (self.titulo)

# serie = Book.objects.create_book("Pride and Prejudice")