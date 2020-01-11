from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import CustomUser
from .forms import UserCreationForm, PartingWordsForm, UserChangeForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from django.views.generic import TemplateView,ListView,DetailView,View
from django.urls import reverse

from django.views.generic.detail import DetailView
from django.views.generic.edit import FormMixin


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'




class PartingWordsView(CreateView):
    
    model = CustomUser
    fields = ['parting_words',]
    template_name = 'PartingWords.html'
    success_url = reverse_lazy('home')



def index(request):
    profile =CustomUser.objects.all()[0:5]
    context = {'profile':profile}
    return render (request, 'home.html', context)







class ProfileDetailView(DetailView):
    template_name = 'profile.html'
    model = CustomUser



#general profile list
def ProfileListView(request):
    profile = CustomUser.objects.filter(is_confirmed = False)
    context = {'profile':profile}
    return render (request, 'ProfileList.html', context)



#list of registered users that have not been verified that can only be viewed on the webpage by a superuser
def UnConfiredProfiles(request):
    profiles = CustomUser.objects.filter(is_confirmed = False)
    context = {'profiles':profiles}
    return render (request, 'users/ProfileList.html', context)



def get_user(request):
    user_qs = CustomUser.objects.filter(user=request.user)
    if user_qs.exists():
        return user_qs.first()
    return None


# class HomeView(TemplateView):
#     template_name = 'index.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         category = Category.objects.all()
#         context['category'] = category
#         return context



        
@login_required
def ContactEdit(request, pk):
    profile = get_object_or_404(CustomUser,  pk=pk)
    if request.method=='POST':
        form = UserChangeForm(request.POST)
        if form.is_valid():
            user_profile=form.save(commit=False)
            user_profile.profile=profile
            user_profile.save()
            return redirect('users:ContactEdit', pk=pk)
    else:
        form = UserChangeForm(instance=request.user)
        context = {'form':form,
                #    'user_profile':user_profile,
                'profile':profile,
                     }
        return render(request, 'ContactEdit.html', context)




class ContactEditView(FormMixin, DetailView):
    template_name='profile.html'
    model = CustomUser
    context_object_name = 'profile'
    form_class = UserChangeForm

    def get_success_url(self):
        return reverse('ContactEditView', kwargs={'pk': self.object.id})

    def get_context_data(self, **kwargs):
        context = super(ContactEditView, self).get_context_data(**kwargs)
        context['form'] = UserChangeForm(initial={'post': self.object})
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.save()
        return super(ContactEditView, self).form_valid(form)


# @login_required
# def ContactEditView(request):
#     user = get_user(request)
#     if request.method== 'POST':
#         form = ContactUpdateForm(request.POST, instance=request.user)
#         if form.is_valid():
#             form.facebook = user_profile
#             form.save()
#             messages.success(request, 'Your account has been successfully updated!')
#             return redirect('users:profile')
#     else:
#         form = ContactUpdateForm(instance=request.user)

#     context= {
#         'form':form,
#         'user':user,
#     }
#     return render(request,'users/ContactForm.html',context)



# def profile(request, profile_pk):
#     profile = get_object_or_404(CustomUser, profile_pk= pk)
#     if request.method== 'POST':
#         form = ContactUpdateForm(request.POST, instance=request.user)
#         if form.is_valid():
#             form.facebook = user_profile
#             form.save()
#             messages.success(request, 'Your account has been successfully updated!')
#             return redirect('users:profile')
#     else:
#         form = ContactUpdateForm(instance=request.user)

#     context= {
#         'form':form,
#         'user':user,
#         'profile':profile
#     }
    
    # context = {'profile': profile}
    # return render(request, 'profile.html', context)