from django.template import *
from django.shortcuts import *

from presentations.models import *
from presentations.forms import *
from presentations.helpers import *

PDF_DIR = 'pdf_files/'
MOVIE_DIR = 'movie_files/'
SLIDE_DIR = 'slide_files/'

def index(request):
    return render_to_response('index.html', context_instance=RequestContext(request))

def login(request):
    return render_to_response('login.html', context_instance=RequestContext(request))

def new(request):
    if request.method == "GET": # wyswietl formularz z doaniem pliku pdf
        upload_presentation_form = UploadPresentationForm()
        return render_to_response('new.html', {'upload_presentation_form': upload_presentation_form}, context_instance=RequestContext(request))

    if(request.method == "POST"):
        # upload_presentation_form = UploadPresentationForm(request.POST, request.FILES)

        title = request.POST['title']
        description = request.POST['description']
        pdf_file = request.FILES['pdf_file']
        movie_file = request.FILES['movie_file']

        pdf_path = save_on_server(pdf_file, PDF_DIR)
        movie_path = save_on_server(movie_file, MOVIE_DIR)

        p = Presentation()
        p.title = title
        p.description = description
        p.pdf_file = pdf_path
        p.movie_file = movie_path
        p.save()

        slide_list = convert(pdf_path, p.id, SLIDE_DIR)

        collect_static()

        return render_to_response('new_slides.html', {'slide_list': slide_list}, context_instance=RequestContext(request))

    return HttpResponse()

def new_slides(request):
    #if request.method == "GET":


    #if request.metod == "POST":




    return HttpResponse("Dodawanie slajdow")