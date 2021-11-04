from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_view

urlpatterns = [
  
    url('register/', views.register, name='register'),
    url('profile/', views.profile, name='profile'),
    url('login/', auth_view.LoginView.as_view(template_name='registration_app/login.html'), name="login"),
    url('logout/', auth_view.LogoutView.as_view(template_name='registration_app/logout.html'), name="logout"),
    url('gallery/', views.gallery, name='gallery'),
      url('', views.home, name='home'),
   
    ]