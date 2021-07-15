from django.contrib.auth import forms
from django.contrib.auth import models
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import User
from django.db.models import fields

class userCreationForm(UserCreationForm):
    password:None
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']
class Admin_Deshbord(UserChangeForm):
    class Meta:
        model=User
        fields='__all__'
class User_Deshbord(UserChangeForm):
    password=None
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']
        label={
            'email':'email'
        }

