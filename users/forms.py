from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from crispy_forms.layout import Field

DEPARTMENT = (
('ELECTRONIC AND COMPUTER','ECE'),
('CHEMICAL AND POLYMER','CPE'),
('MECHANICAL','MECH'),

)


class UserCreationForm(UserCreationForm):
    username = forms.CharField(label = 'username',
                                  
                           max_length = 30,
                           min_length = 5,
                           widget=forms.TextInput(attrs={'class':'form-control' })
                           )
    aka = forms.CharField(label = 'A.K.A',
                           max_length = 30,
                           min_length = 5,
                           widget=forms.TextInput(attrs={'class':'form-control'})
                           )
    first_name = forms.CharField(label = 'first name',
                           max_length = 30,
                           min_length = 5,
                           widget=forms.TextInput(attrs={'class':'form-control'})
                           )
    last_name = forms.CharField(label = 'last name',
                           
                           max_length = 30,
                           min_length = 5,
                           widget=forms.TextInput(attrs={'class':'form-control'})
                           )
    matric = forms.CharField(label = 'matric number',
                            # help_texts =
                            # error_messages =
                            max_length = 9,
                            min_length = 9,
                            widget=forms.TextInput(attrs={'class':'form-control'})
                            )
    department = forms.CharField(
                            # help_texts =
                            # error_messages =
                            # max_length=3,
                            widget=forms.Select(choices=DEPARTMENT, attrs={'class':'form-control'}),
                            label = 'department',
                            )
    email = forms.EmailField(label = 'email',
                            #  help_texts =
                            #  error_messages =
                             max_length = 30,
                             min_length = 5,
                             widget=forms.EmailInput(attrs={'class':'form-control'})
                             )
    password1 = forms.CharField(label = 'password',
                                # help_texts =
                                # error_messages =
                                max_length = 30,
                                min_length = 5,
                                widget=forms.PasswordInput(attrs={'class':'form-control'})
                                )
    password2 = forms.CharField(label = 'cofirm password',
                                # help_texts =
                                # error_messages =
                                max_length = 30,
                                min_length = 5,
                                widget=forms.PasswordInput(attrs={'class':'form-control'})
                                
                                )

    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'matric', 'aka', 'department')
    




class UserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('phone', 'email','linkedin', 'twitter', 'facebook', 'avi')
       

class PartingWordsForm(forms.ModelForm):
    parting_words = forms.CharField(label = 'Words on Marble',
                           max_length = 30,
                           min_length = 5,
                           widget=forms.TextInput(attrs={'class':'form-control' })
                           )
    class meta:
        model = CustomUser
        fields = ('parting_words',)


