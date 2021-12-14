from django.shortcuts import render
from .models import wallpaper


def index(request):
    images = wallpaper.objects.all()

    return render(request, 'index.html')
