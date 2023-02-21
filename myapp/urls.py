from django.urls import path
from . import views

urlpatterns = [
    path('home', views.article_list, name='article_list'),
    path('hello/', views.hello, name='hello'),
    path('goodbye/', views.goodbye, name='goodbye'),
]
