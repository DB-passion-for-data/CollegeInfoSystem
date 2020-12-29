from django.urls import path
from CIS2 import views

urlpatterns = [
    path("", views.Homepage),
    path("TeachersData/",views.TeachersData),
    path("Contactus/",views.Contactus),
    path("About/",views.About)
]