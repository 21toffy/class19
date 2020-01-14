from django.urls import path
from .views import picturedetail
from pictures import views

from pictures.views import PhotoUpload


app_name = 'gallery'

urlpatterns = [
    path('gallery/', views.gallery, name='gallery'),
   
    

    path('gallery/<pk>', views.picturedetail.as_view(), name  = 'profile_detail' ),

    path('upload-picture/', PhotoUpload.A),


    

]
