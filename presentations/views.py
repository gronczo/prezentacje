from django.template import *
from django.shortcuts import *
from presentations.helpers import convert, save_file
from presentations.forms import *
# from presentations import *

# Create your views here.

def index(request):
    return render_to_response('index.html', context_instance=RequestContext(request))

def login(request):
    return render_to_response('login.html', context_instance=RequestContext(request))

def step1(request):
    # wyswietl formularz z dodaniem pliku pdf
    if request.method == "GET": # wyswietl formularz
        upload_pdf_form = UploadPdfForm()
        return render_to_response('step1.html',{'upload_pdf_form': upload_pdf_form}, context_instance=RequestContext(request))

    if request.method == "POST": # otrzymanie danych z formularz
        upload_pdf_form = UploadPdfForm(request.POST, request.FILES)

        if upload_pdf_form.is_valid():
            uploaded_file = request.FILES['pdf_file']
            name = uploaded_file.name
            print "-- views -- step1() -- POST upload file name: " + name
            if name[-3:] != "pdf":
                print "-- views -- step1() -- invalid file format: " + name[-3:]
                return  HttpResponse("Niepoprawny format pliku. Sprawdz czy jest to plik pdf.")

            path = save_file(uploaded_file) # zapisz pdf na serwerze
            file_list = convert(path, name) # zamien pdf na png

            # dodaj prezentacje do bazy danych
            p = Presentation()
            p.pdf_file = name
            p.title = request.POST["title"]
            p.description = request.POST["description"]
            p.user_id = 1
            p.category_id = 1
            p.save()
            print "-- views -- step1 -- Presentation add to database"

            # dodaj slajdu do bazy danych
            for element in file_list:
                slide = Slide()
                slide.presentation = p
                slide.slide_url = element
                slide.time = "00:00"
                slide.save()
                print "-- views -- step1 -- Slide add to database"

            # wyswietl formularz ze slajdami
            return HttpResponse("Dodano do bazy")

        else:
            return HttpResponse("Formularz jest niepoprawnie wyplniony!")
            #return HttpResponseRedirect('../step2.html?id=' + str(p.id) ) # przekieruj i przekaz id prezentacji do kolejnego formularza
    else:
        return  HttpResponse()

def step2(request): # wyswietl formularz ze slajdami
    if request.method == 'POST':
        id = request.POST['id']
        title = request.POST['title']

        p = Presentation.objects.get(pk=id)


        p.save()

        return HttpResponse(str(p.pdf_file))
    else:
        id = request.GET['id']
        return render_to_response('step2.html', {'id':id}, context_instance=RequestContext(request))


