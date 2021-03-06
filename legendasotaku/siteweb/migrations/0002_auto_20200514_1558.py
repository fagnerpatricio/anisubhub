# Generated by Django 2.2.12 on 2020-05-14 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteweb', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='series',
            name='url_anidb',
            field=models.URLField(default='None', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='series',
            name='url_crunchyroll',
            field=models.URLField(default=None, max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='series',
            name='url_imdb',
            field=models.URLField(default=None, max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='series',
            name='url_the_movie_db',
            field=models.URLField(default=None, max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='series',
            name='url_trakt',
            field=models.URLField(default=None, max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='series',
            name='url_tv_maze',
            field=models.URLField(default=None, max_length=500),
            preserve_default=False,
        ),
    ]
