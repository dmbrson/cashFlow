from django.urls import path
from . import views


urlpatterns = [
    path('', views.record_list, name='record_list'),
    path('record/create/', views.record_create, name='record_create'),
    path('get_subcategories/', views.get_subcategories, name='get_subcategories'),
    path('get_categories/', views.get_categories, name='get_categories'),
    path('record/<int:pk>/update/', views.record_update, name='record_update'),
    path('record/<int:pk>/delete/', views.record_delete, name='record_delete'),
]