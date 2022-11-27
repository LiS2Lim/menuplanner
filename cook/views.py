from django.views.generic import ListView
from .models import Photo

class PhotoListView(ListView):
    model = Photo
    template_name = "index.html"
    context_object_name = "photos"
