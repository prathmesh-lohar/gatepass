from django.contrib import admin
from django.urls import path,include
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("",views.home, name="home"),
    path("entry/<int:id>",views.entry, name="entry"),
    path("live_entry",views.live_entry, name="live_entry"),
    path('latest_entry_json', views.latest_entry_json, name='latest_entry_json'),
   
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)    