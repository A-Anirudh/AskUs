from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from .models import Profile
from log.models import Log
from django.contrib.auth.models import User
from allauth.account.decorators import verified_email_required

#CBV IMPORTS BELOW

from django.contrib.messages.views import SuccessMessageMixin

from .forms import UserRegisterForm, ProfileUpdateForm, UserUpdateForm
from django.views.generic.edit import CreateView
from django.views.generic import DetailView, UpdateView
from django.urls import reverse_lazy, reverse

# Login and logout here
from .forms import LoginForm
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

def login(request):
    if request.user.is_authenticated:
        return redirect('home')
    form = LoginForm(request.POST)
    if form.is_valid():
        username = request.POST['username']
        print(username)
        password = request.POST['password']
        user = authenticate(request, username=username, password = password)
        if user is not None:
            print(user)
            auth_login(request, user)
            return redirect('home')
        else:
            print('Wrong credentials')
            return render(request, 'base/login.html', {'form': form})
        # print(form.cleaned_data)
    else:
        print('Form not valid')
    context = {
        'form': form
    }
    return render(request, 'base/login.html',context)
    
def logout(request):
    if not request.user.is_authenticated:
        return redirect('home')
    auth_logout(request)
    return render(request, 'base/logout.html')

class SignUpView(SuccessMessageMixin, CreateView):
  template_name = 'users/register.html'
  success_url = reverse_lazy('login')
  form_class = UserRegisterForm
  success_message = "Your profile was created successfully"





@verified_email_required
@login_required
def profile(request, username):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid and p_form.is_valid():
            u_form.save()
            p_form.save()
            message = messages.success(request, f'Your profile has been updated')
            return redirect('profile', username=username)

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    try:
        profile = User.objects.get(username=username)
    except User.DoesNotExist:
        message = messages.warning(request,f'Profile not found for {username}')

        return redirect('home')
        profile = ''

    # print('profile name: ',profile.username)

    all_post_by_user = Log.objects.filter(author__username=username)
    # print(all_post_by_user)
    context = {
        'u_form' : u_form,
        'p_form' : p_form,
        'profile' : profile, 
        'all_post_by_user' : all_post_by_user
    }

    return render(request, 'users/profile.html', context)


# Profile update view

class ProfileUpdateView(UpdateView):
    model = User
    template_name = "users/profile_update.html"
    success_message = "Your profile was updated successfully"
    slug_url_kwarg = 'username'
    slug_field = 'username' 
    context_object_name = 'profile'
    fields = ['username', 'email']
    second_form_class = ProfileUpdateForm
    success_url = f'/profile/{User}'
    # success_url=reverse_lazy('profile')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["form2"] = ProfileUpdateForm(self.request.POST, self.request.FILES,  instance = self.request.user.profile) 
        return context


    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        form2 = self.second_form_class(request.POST, request.FILES, instance=self.request.user.profile)
        if form2.is_valid():
            profile = form2.save(commit=False)
            profile.user = request.user
            profile.save()
            form = self.get_form()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


    def get_success_url(self):
        self.object = self.get_object()
        form = self.get_form()
        username=form.data['username']
        return reverse("profile", kwargs={'username': username})