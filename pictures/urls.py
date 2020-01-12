from django.urls import path
from .views import picturedetail
from users import views

app_name = 'gallery'

urlpatterns = [
    path('gallery/', views.gallery, name='gallery'),
   
    

    path('gallery/<pk>', views.picturedetail.as_view(), name  = 'profile_detail' ),


    

]
