from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.home_edit, name='home_edit'),

    # Статус
    path('status/', StatusListView.as_view(), name='status_list'),
    path('status/create/', StatusCreateView.as_view(), name='status_create'),
    path('status/<int:pk>/', StatusUpdateView.as_view(), name='status_update'),
    path('status/<int:pk>/delete/', StatusDeleteView.as_view(), name='status_delete'),

    # Тип
    path('type/', TypeListView.as_view(), name='type_list'),
    path('type/create/', TypeCreateView.as_view(), name='type_create'),
    path('type/<int:pk>', TypeUpdateView.as_view(), name='type_update'),
    path('type/<int:pk>/delete/', TypeDeleteView.as_view(), name='type_delete'),

    # Категория
    path('category/', CategoryListView.as_view(), name='category_list'),
    path('category/create/', CategoryCreateView.as_view(), name='category_create'),
    path('category/<int:pk>', CategoryUpdateView.as_view(), name='category_update'),
    path('category/<int:pk>/delete/', CategoryDeleteView.as_view(), name='category_delete'),

    # Подкатегория
    path('subcategory/', SubCategoryListView.as_view(), name='subcategory_list'),
    path('subcategory/create/', SubCategoryCreateView.as_view(), name='subcategory_create'),
    path('subcategory/<int:pk>', SubCategoryUpdateView.as_view(), name='subcategory_update'),
    path('subcategory/<int:pk>/delete/', SubCategoryDeleteView.as_view(), name='subcategory_delete'),
]