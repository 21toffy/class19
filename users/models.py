from django.contrib.auth.models import AbstractUser
from django.db import models
from PIL import Image



DEPARTMENT = (
('ELECTRONIC AND COMPUTER','ECE'),
('CHEMICAL AND POLYMER','CPE'),
('MECHANICAL','MECH'),

)
   


class CustomUser(AbstractUser):
    


    username = models.CharField(max_length = 30, unique = True)
    first_name = models.CharField(max_length = 30, null = True, blank = True)
    last_name = models.CharField(max_length = 30, null = True, blank = True)
    matric = models.CharField(max_length = 9, unique = True)
    aka = models.CharField(max_length=30)
    department = models.CharField(choices=DEPARTMENT, max_length=30)
    phone = models.CharField(max_length=14, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    linkedin = models.URLField(null=True, blank=True)
    twitter = models.CharField(max_length = 30, null=True, blank=True)
    facebook = models.URLField(null=True, blank=True)
    parting_words = models.CharField(max_length = 180)
    avi = models.ImageField(default='null', upload_to = 'profile_pics')
    is_confirmed = models.BooleanField('confirmation status', default=False)

    USERNAME_FIELD = 'matric'

    def __str__(self):
        return self.username
        



    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)

    #     img = Image.open(self.profile_pic.path)
    #     if img.height >100 or img.width>100:
    #         output_size = (200,200)
    #         img.thumbnail(output_size)
    #         img.save(self.profile_pic.path)

    
    

