from __future__ import unicode_literals
from djongo import models

class Series(models.Model):
    created_at = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False,auto_now=True)

    titulo = models.CharField(max_length=500,null=True)
    temporada = models.IntegerField(default=1,null=True)
    url_the_movie_db = models.URLField(max_length = 500, blank=True)
    url_trakt = models.URLField(max_length = 500, blank=True)
    url_imdb = models.URLField(max_length = 500, blank=True)
    url_tv_maze = models.URLField(max_length = 500, blank=True)
    url_crunchyroll = models.URLField(max_length = 500, blank=True)
    url_anidb = models.URLField(max_length = 500, blank=True)
    url_my_anime_list = models.URLField(max_length = 500, blank=True)
    arquivo_banner = models.ImageField(upload_to='legendasotaku/siteweb/templates/img/banners')
    #arquivo_do_banner = models.FilePathField(max_length=500, blank=False)

    def save(self, *args, **kwargs):
        print("Hello")

    def __str__(self):
        return (self.titulo + " -- (" + str(self.temporada) + "º Temporada)")
    