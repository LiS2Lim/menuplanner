from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Photo
import random

class PhotoListView(ListView):
    model = Photo
    ordering = ['-created_at']
    template_name = "photo_list.html"
    context_object_name = "photos"

class PhotoDetailView(DetailView):
    model = Photo
    template_name = "photo_detail.html"
    context_object_name = "photo"

def Random(req):
    context = random.choice(Photo.objects.all())
    return render(req, 'random.html',{'photo':context})
