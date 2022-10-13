from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("create/", views.create, name="create"),
    path("stafflist/", views.staff_list, name="staff_list"),
    path("comics/", views.comics, name="comics"),
    path("logout/", views.logout_now, name="logout_now"),
    path("help/", views.help, name="help"),
]
