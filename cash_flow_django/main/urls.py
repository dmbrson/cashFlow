from django.urls import path
from . import views


urlpatterns = [
    path('', views.record_list, name='record_list'),
    path('record/create/', views.record_create, name='record_create'),
    path('get_subcategories/', views.get_subcategories, name='get_subcategories'),
]