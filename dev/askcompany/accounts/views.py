from django.contrib.auth import get_user_model,login as auth_login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView,UpdateView,CreateView
from accounts.forms import ProfileForm
from accounts.models import Profile 
from django.shortcuts import redirect
from django.conf import settings
# Create your views here.
# @login_required
# def profile(request) :
#     return render(request,'accounts/profile.html' )

User= get_user_model()
class ProfileView(LoginRequiredMixin,TemplateView) :
    template_name = 'accounts/profile.html'

profile = ProfileView.as_view()

# class ProfileUpdateView(UpdateView):
#     model = Profile 
#     form_class = ProfileForm 

# profile_edit = ProfileUpdateView.as_view()

@login_required
def profile_edit(request):
    try :
        profile = request.user.profile 
    except  Profile.DoesNotExits :
        profile = None
    
    if request.method =="POST":
        form =  ProfileForm(request.POST,request.FILES,instance=profile)
        if form.is_valid():
            profile =form.save( commit=False)
            profile.user = request.user
            profile.save()
            return redirect("profile")
    else :
            form = ProfileForm(instance=profile)
    return render(request, 'accounts/profile_form.html',{
            'form': form, 
        })

class SignupView(CreateView):
    
    model = User ,
    form_class= UserCreationForm,
    success_url= settings.LOGIN_REDIRECT_URL,
    template_name ='accounts/signup_form.html',
    def form_valid(self, form):
        
        response = super().form_valid(form)
        user = self.object
        auth_login(self.request,user )
        return response

signup= SignupView.as_view()
# def signup(request):
#     pass
def logout(requset):
    pass