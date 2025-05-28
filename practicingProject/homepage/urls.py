from django.urls import path

from practicingProject.homepage import views
urlpatterns = [
    path('', views.homepage, name='homepage'),
]