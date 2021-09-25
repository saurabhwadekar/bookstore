from django.shortcuts import render,HttpResponse,HttpResponseRedirect

# Create your views here.


def home(request):
    return HttpResponse("<h1>This is home page</h1>")

def create_aucount(request):
    return render(request,"create_acount.html")

def login_aucount(request):
    return HttpResponseRedirect("/")


    



















