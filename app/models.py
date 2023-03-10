from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class PhotoGallery(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=245, null=True, blank=True)
    image = models.ImageField(verbose_name='image', upload_to='images')
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):  
        return self.name  