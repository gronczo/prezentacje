from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    title = models.CharField(max_length=255) # tytul kategorii
    class Meta:
        verbose_name = "Kategoria"

class Presentation(models.Model):
    title = models.CharField(max_length=255) # tytul prezentacji
    description = models.TextField() # opis prezentacji
    #auth_user = models.ForeignKey(User) # id uzytkownika
    pdf_file = models.CharField(max_length=255) # adres do pliku pdf
    movie_file = models.CharField(max_length=255) # adres do pliku video lub mp3
    #category = models.ForeignKey(Category) # id kategorii
    class Meta:
        verbose_name = "Prezentacja"

class Slides(models.Model):
    presentation = models.ForeignKey(Presentation) # id prezentacji
    slide_file = models.CharField(max_length=255) # adres do pliku png
    time = models.TimeField() # czas wystapienia
    class Meta:
        verbose_name = "Slajd"

class Comment(models.Model):
    auth_user = models.ForeignKey(User) # id uzytkownika
    content = models.CharField(max_length=255) # tresc komentarze
    presentation = models.ForeignKey(Presentation) # id prezentacji
    class Meta:
        verbose_name = "Komentarz"
