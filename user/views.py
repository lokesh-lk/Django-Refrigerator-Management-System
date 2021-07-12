#from django.contrib.auth import forms
#from django.forms.forms import Form
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account has been created for {username}. Continue to login')
            return redirect('user-login')
    else:
        form = CreateUserForm
    context = {
        'form' : form
    }
    return render(request, 'user/register.html', context)

    
def profile(request):
    return render(request,'user/profile.html')

#def profile_update(request):
    if request.method=='POST':
        user_form = UserUpdateForm(request.POST)
        profile_form = ProfileUpdateForm(request.POST,request.FILES)
    else:
        user_form = UserUpdateForm()
        profile_form = ProfileUpdateForm()
    context = {
        'user_form' : user_form,
        'profile_form': profile_form,
    }
    return render(request, 'user/profile_update.html', context)