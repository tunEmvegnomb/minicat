
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('post/', views.post, name='post'),
    path('get_catfact/', views.get_catfact, name='get_catfact')
]