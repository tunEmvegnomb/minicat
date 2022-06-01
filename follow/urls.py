from django.urls import path
from . import views

urlpatterns = [
    path('follow/', views.view_test_follow, name='view_follow'),
]