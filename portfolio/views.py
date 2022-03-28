from django.shortcuts import render
from .models import Image

def home(request):
    return render(request, "index.html")

def get_category(request, cat):
    photos = Image.objects.filter(category=cat)

    context = {
            'category': cat,
            'photos': photos
        }

    return render(request, 'category.html', context)

