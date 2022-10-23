"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from content.views import index
from rest_framework.authtoken import views
# from score.views import detail,update_score

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-token-auth', views.obtain_auth_token),
    path('api-auth',include('rest_framework.urls')), # this adds the login button in browsable api
    path('', index),
    # path('detail', detail),
    path('score/', include('score.urls')),
    path('user/', include('user.urls')),
    path('contens/', include('content.urls')),
]
