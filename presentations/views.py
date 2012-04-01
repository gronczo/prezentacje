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

        for element in slide_list:
            slide = Slide()
            slide.presentation = p
            slide.slide_file = element
            slide.save()

        collect_static()

        return render_to_response('new_slides.html', {'slide_list': slide_list, 'presentation_id': p.id}, context_instance=RequestContext(request))

    return HttpResponse()

def new_slides(request):
    if request.method == "POST":
        presentation_id = request.POST["presentation_id"]
        print "-- views -- new_slides() -- id prezentacji: " + presentation_id

        p = Presentation.objects.filter(id = presentation_id)

        slides = Slide.objects.filter(presentation = p)

        for slide in slides:
            time = request.POST[str(slide.slide_file)]
            slide.time = time
            slide.save()

    return HttpResponse()

def play(request, id):
    if request.method == "GET":
        presentation_id = id

        p = Presentation.objects.filter(id = presentation_id)

    return HttpResponse("Odwarzanie prezentacji o id:  " + presentation_id)

def show(request, id):
    if request.method == "GET":
        presentation_id = id
        p_list = Presentation.objects.filter(id = presentation_id)

        if p_list.count() > 0:
            p = p_list[0]
            return render_to_response('show.html', {'title': p.title, 'description': p.description, 'pdf_file': p.pdf_file, 'movie_file': p.movie_file}, context_instance=RequestContext(request))

        return HttpResponse("Brak prezentacji o podanym id.")

    return HttpResponse()
