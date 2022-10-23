from django.urls import path
from . import views

urlpatterns = [
    path('get_contents', views.get_contents),
]
