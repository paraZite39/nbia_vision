from django.shortcuts import render
from .models import Image, Category

def home(request):
    return render(request, "index.html")

def get_category(request, cat):
    category = Category.objects.get(name=cat)

    context = {
            'category': category,
    }

    return render(request, 'category.html', context)

