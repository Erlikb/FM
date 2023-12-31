"""
URL configuration for djangofm project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from tasks import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.singin, name='singin'),
    path('singup/', views.singup, name='singup'),
    path('home/', views.home, name='home'),
    path('task1/', views.task1, name='task1'),
    path('task2/', views.task2, name='task2'),
    path('task3/', views.task3, name='task3'),
    path('task4/', views.task4, name='task4'),
    path('task5/', views.task5, name='task5'),
    path('task6/', views.task6, name='task6'),
]
