from django.urls import path,include
from . import views

urlpatterns = [
    path('submit_score', views.submit_score),
]
