from django.db import models
from PIL import Image

from users.models import CustomUser

class Album(models.Model):
    picture1 = models.ImageField(upload_to = 'Album_pictures')
    picture2 = models.ImageField(upload_to = 'Album_pictures' , null=True, blank=True)
    picture3 = models.ImageField(upload_to = 'Album_pictures' , null=True, blank=True)
    picture4 = models.ImageField(upload_to = 'Album_pictures' , null=True, blank=True)
    tag = models.CharField(max_length=100)
    uploaded = models.DateField(auto_now_add=True)