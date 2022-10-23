

from django.urls import path
from user import views

urlpatterns = [
    path('sign_up', views.create_user),
    path('login', views.login),
    path('forget_password', views.forget_password),
    path('change_password', views.change_password),
    path('access_levels', views.access_levels),
]
