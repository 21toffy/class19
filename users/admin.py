from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import UserCreationForm, UserChangeForm, PartingWordsForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    parting_words_form = PartingWordsForm
    model = CustomUser
    list_display = ['username','first_name', 'last_name', 'email', 'matric', 'aka', 'department' ,'phone', 'email','linkedin', 'twitter', 'facebook', 'avi', 'parting_words',]

admin.site.register(CustomUser, CustomUserAdmin)



