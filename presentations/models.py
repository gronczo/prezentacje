from django.db import models
from prezentacje.settings import *

class Presentation(models.Model):
    title = models.CharField(max_length=255, verbose_name='Tytul') # tytul prezentacji
    description = models.TextField(verbose_name='Opis') # opis prezentacji
    move_url = models.URLField(verify_exists=False, verbose_name='Adres_filmu') # adres url do filmu
    movie_file = models.FileField(upload_to='media')
    pdf_url = models.URLField(verify_exists=False, verbose_name='Adres pdf') # adres url do prezentacji w pdf
    pdf_file = models.CharField(max_length=255)
    user_id = models.IntegerField(verbose_name='Id_uzytkownika') # id uzytkownika ktory dodal prezentacje
    category_id = models.IntegerField(verbose_name='Id_kategorii') # id kategorii do ktorej nalezy prezentacja
    class Meta:
        verbose_name = "Prezentacja"
        verbose_name_plural = "Prezentacje"
    # def __str__(self):
    #     return self.title
    #def __unicode__(self):
    #    return self.title

class Slide(models.Model):
    presentation = models.ForeignKey(Presentation, verbose_name='Prezentacja') # adres id prezentacji do ktorej nalezy slajd
    slide_url = models.CharField(max_length=255) # adres url do slajdu (borazka jpg)
    time = models.TimeField(verbose_name='Czas_wystapienia') # czas wystapienia
    title = models.CharField(max_length=255, verbose_name='Tytul') # tytul slajdu
    class Meta:
        verbose_name = "Slajd"
        verbose_name_plural = "Slajdy"
    # def __str__(self):
    #     return self.title
    def __unicode__(self):
        return  self.title


class Attachment(models.Model):
    title = models.CharField(max_length=255)
    attached_file = models.FileField(upload_to='attachments')