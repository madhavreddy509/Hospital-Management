from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User,Blog,Appointment

from django.forms import ModelForm


class LoginForm(forms.Form):
    username = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    firstname = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    lastname = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    address = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    class Meta:
        model = User
        fields = ('username', 'email','firstname','lastname', 'password1', 'password2', 'is_patient', 'is_doctor')



class BlogForm (ModelForm):
    class Meta:
        model=Blog
        fields =['title','description','featured_image','select_category','draft']
        

    def __init__(self,*args,**kwargs):
        super(BlogForm, self).__init__(*args,**kwargs)

        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input'})

class CategoryForm(ModelForm):
    class Meta:
        model=Blog
        fields=['select_category']
    
    def __init__(self,*args,**kwargs):
        super(CategoryForm, self).__init__(*args,**kwargs)

        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input'})

class AppointmentForm (ModelForm):
    class Meta:
        model=Appointment
        fields =['date','select_category','description']
        

    def __init__(self,*args,**kwargs):
        super(AppointmentForm, self).__init__(*args,**kwargs)

        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input'})