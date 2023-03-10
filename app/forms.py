from django.forms import ModelForm
from .models import PhotoGallery


class GalleryImageForm(ModelForm):  
    class Meta:  
        # To specify the model to be used to create form  
        model = PhotoGallery  
        # fields = ['image']  
        fields = '__all__'