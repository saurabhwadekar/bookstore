from django.shortcuts import get_object_or_404, render,HttpResponse,HttpResponseRedirect
from .models import Book
from .forms import UserLoginForm,UserMakeForm,BookForm
from django.contrib.auth import authenticate, login, logout
from django.http import FileResponse

# Create your views here.


def home(request):
    if request.user.is_authenticated == False:
        return HttpResponseRedirect("/login-aucount/")
    data = Book.objects.all()
    dict_data = {
        "data":data,
    }
    return render(request,"home.html",dict_data)

def add_book(request):
    if request.user.is_authenticated == False:
        return HttpResponseRedirect("/login-aucount/")
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
    if request.user.is_authenticated == False:
        return HttpResponseRedirect("/login-aucount/")
    if request.method == "POST":
        del_obj = Book.objects.get(id=id)
        del_obj.delete()
    return HttpResponseRedirect("/")

def update_book(request,id):
    if request.user.is_authenticated == False:
        return HttpResponseRedirect("/login-aucount/")
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
    if request.user.is_authenticated:
        return HttpResponseRedirect("/")
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
    if request.user.is_authenticated:
        return HttpResponseRedirect("/")
    ulf  = UserLoginForm()
    if request.method == "POST":
        ulf = UserLoginForm(request=request,data=request.POST)
        if ulf.is_valid():
            username = ulf.cleaned_data["username"]
            password = ulf.cleaned_data["password"]
            user = authenticate(username=username,password=password)
            if user.is_authenticated:
                login(request=request,user=user)
                return HttpResponseRedirect("/")
    dict_data = {
        "ulf":ulf,
    }
    return render(request,"login_aucount.html",dict_data)

def logout_aucount(request):
    if request.user.is_authenticated == False:
        return HttpResponseRedirect("/login-aucount/")
    if request.method == "POST":
        logout(request)
        return HttpResponseRedirect("/login-aucount/")
    return HttpResponseRedirect("/")

def sec_cover(request,file_name):
    if request.user.is_authenticated:
        print(file_name)
        file_obj = get_object_or_404(Book,cover="cover/"+file_name)
        return FileResponse(file_obj.cover)
    return HttpResponseRedirect("/")
    



















