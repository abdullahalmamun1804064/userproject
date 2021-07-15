from .models import blog
from django.contrib.auth import authenticate, update_session_auth_hash
from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm, UserCreationForm,UserChangeForm
from django.contrib.auth.models import User,Group
from django.contrib.auth import login,logout
from django.contrib import messages

from . import forms


def home (request):
    dic={
          "page" : 'Welcome our Website',
    }
    return render(request , "enroll/index.html", dic)

#signup page
def user_signup(request):
    if request.method=="POST":
        fm=forms.userCreationForm(request.POST)
        if fm.is_valid():
            user=fm.save()
            group=Group.objects.get(name='manager')
            user.groups.add(group)

            messages.success(request,"Successfully Signup !!!")
    else:
        fm=forms.userCreationForm()

    dic={
       'form':fm,
       'page':"Singup your information",

    }
    return render(request,'enroll/signup.html',dic)

#loging page

def user_login(request):
    
    if request.method=="POST":
        fm=AuthenticationForm(request=request,data=request.POST)
        if fm.is_valid():
            un=fm.cleaned_data['username']
            up=fm.cleaned_data['password']
            user=authenticate(username=un,password=up)
            if user is not None:
                login(request,user)
                messages.success(request,"Successfully Loging !!!")
                return HttpResponseRedirect('/el/deshbord/')
    else:
        fm=AuthenticationForm()

    dic={
       'form':fm,
       'page':"Login your account ",

    }
    return render(request,'enroll/login.html',dic)



#deshbord
def user_deshbord(request):
        if request.user.is_authenticated:
            if request.method =='POST':
                if request.user.is_superuser:
                    fm=forms.Admin_Deshbord(request.POST,instance=request.user)
                    user=User.objects.all()
                else:
                    fm=forms.User_Deshbord(request.POST,instance=request.user)
                    user=None

                if fm.is_valid():
                    fm.save()
                    messages.success(request,'Profile successfully update !!!')
            else:
                if request.user.is_superuser:
                    fm=forms.Admin_Deshbord(instance=request.user)
                    user=User.objects.all()
                else:
                    fm=forms.User_Deshbord(instance=request.user)
                    user=None

            name=request.user
            dic={
                'form':fm,
                'page':"Deshbord" ,
                'name':name,
                 'user':user
                }
            return render(request,'enroll/deshbord.html',dic)
        else:
            return HttpResponseRedirect("/el/login/")




#change password with old password
def change_pass_with_old_pass(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            fm=PasswordChangeForm(user=request.user , data= request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request,fm.user)
                messages.success(request,'Password successfully Update!!!')
                return HttpResponseRedirect("/el/deshbord/")
        else:
            fm=PasswordChangeForm(user=request.user )
        dic={
            'form':fm,
            'page':'Update your password',
        }
        return render(request,'enroll/password.html',dic)
    else:
        return HttpResponseRedirect('/el/login/')
#change password without old password
def change_pass_without_old_pass(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            fm=SetPasswordForm(user=request.user , data= request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request,fm.user)
                messages.success(request,'Password successfully Update!!!')
                return HttpResponseRedirect("/el/deshbord/")
        else:
            fm=SetPasswordForm(user=request.user )
        dic={
            'form':fm,
            'page':'Update your password',
        }
        return render(request,'enroll/password.html',dic)
    else:
        return HttpResponseRedirect('/el/login/')

#logout
def user_logout(request):
    logout(request)
    return HttpResponseRedirect("/co/login/")

#User details

def user_details(request,id):
    if request.user.is_authenticated:
        pi=User.objects.get(pk=id)
        fm=forms.Admin_Deshbord(instance=pi)
        name=pi.username
        dic={  
            "form":fm,
            'page':'Deshbord',
            'name':name  
        }
        return render(request,'enroll/user_details.html',dic)
    else:
        return HttpResponseRedirect('/el/login/')

