from django.template import *
from django.shortcuts import *

# Create your views here.

def index(request):
    return render_to_response('index.html', context_instance=RequestContext(request))

def login(request):
    return render_to_response('login.html', context_instance=RequestContext(request))