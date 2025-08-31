"""
URL configuration for todo_proj_django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.urls import path, include
from django.views import View
from django.contrib.auth import views as auth_views, login

from tasks.views import logout_confirm


class SignUpView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, "registration/signup.html", {"form": form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("tasks:list")
        return render(request, "registration/signup.html", {"form": form})


urlpatterns = [
    path('admin/', admin.site.urls),

    # Authentication
    path('login/', auth_views.LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('logout/', logout_confirm, name='logout'),

    path("", include("tasks.urls"))
]
