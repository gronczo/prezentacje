from django.template import *
from django.shortcuts import *
from presentations.forms import *

# Create your views here.

def index(request):
    return render_to_response('index.html', context_instance=RequestContext(request))

def login(request):
    return render_to_response('login.html', context_instance=RequestContext(request))

def step1(request): # wyswietl formularz z doaniem pliku pdf
    if request.method == "GET": # wyswietl formularz
        return render_to_response('step1.html', context_instance=RequestContext(request))
    elif(request.method == "POST" and 'pdf_file' in request.FILES): # otrzymanie danych z formularz
        f = request.FILES['pdf_file']
        p = Presentation()
        p.pdf_file = f
        p.user_id = 1
        p.category_id = 1
        p.save()

        # przetworzenie pliku pdf

        return HttpResponseRedirect('../step2.html?id=' + str(p.id) ) # przekieruj i przekaz id prezentacji do kolejnego formularza
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


