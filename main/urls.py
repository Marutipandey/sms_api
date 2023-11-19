"""
URL configuration for main project.

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
from mainapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('register', views.sms_list, name='sms_list'),
    path('sms/<int:pk>/', views.sms_detail, name='sms_detail'),
    path('sms/new/', views.sms_new, name='sms_new'),
    path('sms/<int:pk>/edit/', views.sms_edit, name='sms_edit'),
    path('sms/<int:pk>/delete/', views.sms_delete, name='sms_delete'),
    path("", views.register_request, name="register"),
    path("login", views.login_request, name="login"),
    path("logout", views.logout_request, name= "logout"),

]
