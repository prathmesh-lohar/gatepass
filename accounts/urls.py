from django.contrib import admin
from django.urls import path,include
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('register', views.register, name='register'),
    path('adhar_verify', views.adhar_verify, name='adhar_verify'),
    path('profile_register', views.profile_register, name='profile_register'),
    
    # path('register', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
   
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)    