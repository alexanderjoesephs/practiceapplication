from django.shortcuts import render, HttpResponse
from .models import Song
# Create your views here.

def index(request):
    songs = Song.objects.filter().all
    return render(request, 'mainpage/index.html', {"songs":songs})