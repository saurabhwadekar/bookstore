from django.urls import path
from . import views

urlpatterns = [
    path("",views.home),
    path("add-book/",views.add_book,name="addbook"),
    path("delete-book/<int:id>/",views.delete_book,name="deletebook"),
    path("update-book/<int:id>/",views.update_book,name="updatebook"),
    path("create-aucount/",views.create_aucount,name="createaucont"),
    path("login-aucount/",views.login_aucount,name="loginaucont"),
    path("logout-aucount/",views.logout_aucount,name="logoutaucont"),
    path("media/cover/<str:file_name>/",views.sec_cover,name="seccover"),
]
