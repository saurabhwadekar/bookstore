from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.forms import widgets
from .models import Book



class UserMakeForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username","password1","password2","first_name","last_name","email")
        
class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"class":"usernameclass"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"passinputclass"}))

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ("title","info","cover","book_pdf")
        widgets = {
            "title":forms.TextInput(attrs={"class":"titleclass",}),
            "info":forms.Textarea(attrs={"class":"infoclass",}),
        }

















