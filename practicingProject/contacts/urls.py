from django.urls import path
from practicingProject.contacts import views

urlpatterns = [
    path('', views.contact_details),
]