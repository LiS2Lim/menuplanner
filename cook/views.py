from django.views.generic import ListView
from .models import Photo

class PhotoListView(ListView):
    model = Photo
    ordering = ['-created_at']
    template_name = "index.html"
    context_object_name = "photos"
