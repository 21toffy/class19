from django.urls import path
from .views import SignUpView, PartingWordsView, ProfileDetailView, ContactEditView
from users import views

app_name = 'users'

urlpatterns = [
    path('home/', views.index, name='index'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('PartingWords/', PartingWordsView.as_view(), name='PartingWords'),
    # path('profile/<int:profile_pk>', views.profile, name='profile'),
    
    path('ProfileList/', views.ProfileListView, name='ProfileListView'),
    path('UnConfiredProfiles/', views.UnConfiredProfiles, name='UnConfiredProfiles'),

    path('profle-detail/<pk>', views.ProfileDetailView.as_view(), name  = 'profile_detail' ),


    path('edit-contact/<pk>/', views.ContactEdit, name = 'ContactEdit'),
    
    path('edit-my-contact/<pk>', ContactEditView.as_view(), name='ContactEditView'),

]
