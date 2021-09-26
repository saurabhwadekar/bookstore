from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from .models import Book
from .forms import UserLoginForm,UserMakeForm,BookForm

# Create your views here.


def home(request):
    data = Book.objects.all()
    dict_data = {
        "data":data,
    }
    return render(request,"home.html",dict_data)

def add_book(request):
    bf = BookForm()
    dict_data = {
        "bf":bf
    }
    return render(request,"add_book.html",dict_data)

def create_aucount(request):
    return render(request,"create_acount.html")

def login_aucount(request):
    return HttpResponseRedirect("/")


    



















