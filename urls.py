
from django.urls import path
from .import views

urlpatterns = [
     path("register.html/",views.register, name="tieupRegister"),
     path("login.html/",views.login, name="tieupLogin"),
     path("", views.index, name="tieupHome"),
     path("profile.html/", views.profile, name="See your profile"),
     path("events/", views.events, name="Upcoming Events")


]