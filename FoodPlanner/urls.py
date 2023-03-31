"""FoodPlanner URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from FoodGenerator.views import food
from FoodGenerator.views import book
from FoodGenerator.views import kalender
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from FoodGenerator.views import register, login_view, profile, datenschutz
from django.urls import reverse_lazy
from FoodGenerator.views import CustomLogoutView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', food),
    path('food/', food, name='food'),
    path('rezeptbuch',book),
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('profile/', profile, name='profile'),
    path('kalender/', kalender, name='kalender'),
    path('register/', register, name='register'),
    path('datenschutz',datenschutz),
]
