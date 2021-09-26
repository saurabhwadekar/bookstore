from django.urls import path
from . import views

urlpatterns = [
    path("",views.home),
    path("add-book/",views.add_book,name="addbook"),
    path("create-aucount/",views.create_aucount,name="createaucont"),
    path("login-aucount/",views.login_aucount,name="createaucont"),

]
