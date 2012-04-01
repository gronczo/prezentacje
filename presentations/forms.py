from django import forms

class UploadPresentationForm(forms.Form):
    title = forms.CharField(max_length=255)
    description = forms.CharField(max_length=255)
    pdf_file = forms.FileField()
    movie_file = forms.FileField()

class ShowPresentationForm(forms.Form):
    title = forms.CharField(max_length=255)
    description = forms.CharField(max_length=255)
    pdf_file = forms.CharField(max_length=255)
    movie_file = forms.CharField(max_length=255)
