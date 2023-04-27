import django_filters
from django import forms
from .models import mediaAnime
from users.models import List

class listFilter(django_filters.FilterSet):
    GENRE_CHOICES = [
        ('', '--------'),
        ('Action', 'Action'),
        ('Adventure', 'Adventure'),
        ('Comedy', 'Comedy'),
        ('Drama', 'Drama'),
        ('Fantasy', 'Fantasy'),
        ('Historical', 'Historical'),
        ('Magic', 'Magic'),
        ('Martial Arts', 'Martial Arts'),
        ('Mecha', 'Mecha'),
        ('Military', 'Military'),
        ('Music', 'Music'),
        ('Parody', 'Parody'),
        ('Romance ', 'Romance'),
        ('Samurai', 'Samurai'),
        ('School', 'School'),
        ('Sci-Fi', 'Sci-Fi'),
        ('Seinen', 'Seinen'),
        ('Shounen', 'Shounen'),
        ('Slice of Life', 'Slice of Life'),
        ('Space', 'Space'), ('Sports', 'Sports'),
        ('Super Power', 'Super Power'),
        ('Supernatural', 'Supernatural'),
        ('Thriller', 'Thriller'),
        ('Vampire', 'Vampire'),
    ]
    TYPE_CHOICES = [
        ('TV','TV'),
        ('Movie','Movie'),
        ('OVA','OVA'),
    ]
    genre = django_filters.MultipleChoiceFilter(lookup_expr="contains", conjoined=True, choices = GENRE_CHOICES)
    type = django_filters.ChoiceFilter(choices = TYPE_CHOICES)
    class Meta:
        model = mediaAnime
        fields = ['name', 'genre', 'type']
