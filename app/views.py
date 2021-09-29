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
    if request.method == "POST":
        bf = BookForm(request.POST,request.FILES)
        if bf.is_valid():
            bf.save()
            return HttpResponseRedirect("/")

    dict_data = {
        "bf":bf
    }
    return render(request,"add_book.html",dict_data)

def delete_book(request,id):
    if request.method == "POST":
        del_obj = Book.objects.get(id=id)
        del_obj.delete()
    return HttpResponseRedirect("/")

def update_book(request,id):
    ub_obj = Book.objects.get(id = id)
    ubf = BookForm(instance=ub_obj)
    if request.method == "POST":
        ubf = BookForm(request.POST,request.FILES,instance=ub_obj)
        if ubf.is_valid():
            ubf.save()
            return HttpResponseRedirect("/")
    dict_data = {
        "ubf":ubf,
        "id":id
    }
    return render(request,"update_book.html",dict_data)

def create_aucount(request):
    umf = UserMakeForm()
    if request.method == "POST":
        umf = UserMakeForm(request.POST)
        if umf.is_valid():
            umf.save()
            return HttpResponseRedirect("/")
    dict_data = {
        "umf":umf,
    }
    return render(request,"create_acount.html",dict_data)

def login_aucount(request):
    return HttpResponseRedirect("/")


    



















