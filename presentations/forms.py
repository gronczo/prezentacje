from django import forms
from django.contrib.admin.widgets import *
from presentations.models import *
from prezentacje.settings import *

class PresentationForm(forms.ModelForm):
    class Meta:
        model = Presentation
    #title = forms.CharField() # tytul prezentacji
    #description = forms.CharField() # opis prezentacji
    #move_url = forms.URLField() # adres url do filmu
    #pdf_url = forms.URLField() # adres url do prezentacji w pdf
    # user_id = forms.IntegerField(verbose_name='Id_uzytkownika') # id uzytkownika ktory dodal prezentacje
    #category_id = forms.IntegerField() # id kategorii do ktorej nalezy prezentacja
    # video = forms.Field(widget=forms.FileInput, required=False)
    #pdf_file = forms.FileField()

#class UploadPdfForm(forms.ModelForm):
#    class Meta:
#        model = Presentation
#        fields = ('pdf_file',)


class UploadPdfForm(forms.Form):
    title = forms.CharField(max_length=255)
    description = forms.CharField(max_length=255)
    pdf_file = forms.FileField()

#class PresentationForm(forms.Form)