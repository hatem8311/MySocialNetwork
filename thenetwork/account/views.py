from django.shortcuts import render, redirect
from account.froms import (

RegisterationFrom ,
EditProfileForm
)
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm,PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method =='POST':
        form = RegisterationFrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home')
    else:
        form = RegisterationFrom()
    ## i thin that  this line is for to pass the data in the form to the data base    
    args = {'form': form}
    return render(request, 'account/reg_from.html', args)


def view_profile(request, pk=None):
    if pk:
        user=User.objects.get(pk=pk)
    else:
        user= request.user
    args = {'user':user}
    return render(request, 'account/profile.html', args)

def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect(reverse('accounts:view_profile'))
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'account/edit_profile.html', args)
def change_password(request):
    ##i think that the post method is a function in PasswordChangeForm
    if request.method == 'POST':
        form = PasswordChangeForm(data = request.POST,user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request , form.user)
            return redirect(reverse('account:view_profile'))
        else:
            return redirect(reverse('account:change_password'))
    else:
        form = PasswordChangeForm(user=request.user)

        args = {'form': form}
        return render(request, 'account/change_password.html', args)
