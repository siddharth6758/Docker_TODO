from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('toggle/<int:pk>/', views.toggle, name='toggle'),
    path('delete/<int:pk>/', views.delete_item, name='delete'),
]