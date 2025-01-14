from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from main.models import Status, Type, Category, SubCategory
from .forms import StatusForm, TypeForm, CategoryForm, SubCategoryForm

def home_edit(request):
    return render(request, 'edit/edit_home.html', {})

# Общий базовый класс для списков
class BaseListView(ListView):
    template_name = 'edit/base_list.html'
    context_object_name = 'objects'

    # Динамически определяем названия модели и URL
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = self.model._meta.verbose_name_plural
        context['create_url'] = f"{self.model.__name__.lower()}_create"
        context['update_url'] = f"{self.model.__name__.lower()}_update"
        context['delete_url'] = f"{self.model.__name__.lower()}_delete"

        # Устанавливаем связь с зависимыми полями, если они есть
        if self.model == Category:
            context['has_related'] = True
            context['related_fields'] = [{'name': 'type', 'label': 'Тип'}]
        elif self.model == SubCategory:
            context['has_related'] = True
            context['related_fields'] = [
                {'name': 'category', 'label': 'Категория'},
                {'name': 'type', 'label': 'Тип'},
            ]
        else:
            context['has_related'] = False
        return context

# Общий базовый класс для создания
class BaseCreateView(CreateView):
    template_name = 'edit/base_form.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = self.model._meta.verbose_name
        context['list_url'] = f"{self.model.__name__.lower()}_list"
        return context

# Общий базовый класс для редактирования
class BaseUpdateView(UpdateView):
    template_name = 'edit/base_form.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = self.model._meta.verbose_name
        context['list_url'] = f"{self.model.__name__.lower()}_list"
        return context

# Общий базовый класс для удаления
class BaseDeleteView(DeleteView):
    template_name = 'edit/base_confirm_delete.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = self.model._meta.verbose_name
        context['list_url'] = f"{self.model.__name__.lower()}_list"
        return context

# CRUD для статусов
class StatusListView(BaseListView):
    model = Status

class StatusCreateView(BaseCreateView):
    model = Status
    form_class = StatusForm
    success_url = reverse_lazy('status_list')

class StatusUpdateView(BaseUpdateView):
    model = Status
    form_class = StatusForm
    success_url = reverse_lazy('status_list')

class StatusDeleteView(BaseDeleteView):
    model = Status
    success_url = reverse_lazy('status_list')

# CRUD для типов
class TypeListView(BaseListView):
    model = Type

class TypeCreateView(BaseCreateView):
    model = Type
    form_class = TypeForm
    success_url = reverse_lazy('type_list')

class TypeUpdateView(BaseUpdateView):
    model = Type
    form_class = TypeForm
    success_url = reverse_lazy('type_list')

class TypeDeleteView(BaseDeleteView):
    model = Type
    success_url = reverse_lazy('type_list')

# CRUD для категорий
class CategoryListView(BaseListView):
    model = Category
    template_name = 'edit/base_list.html'

class CategoryCreateView(BaseCreateView):
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy('category_list')

class CategoryUpdateView(BaseUpdateView):
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy('category_list')

class CategoryDeleteView(BaseDeleteView):
    model = Category
    success_url = reverse_lazy('category_list')

# CRUD для подкатегорий
class SubCategoryListView(BaseListView):
    model = SubCategory
    template_name = 'edit/base_list.html'

class SubCategoryCreateView(BaseCreateView):
    model = SubCategory
    form_class = SubCategoryForm
    success_url = reverse_lazy('subcategory_list')

class SubCategoryUpdateView(BaseUpdateView):
    model = SubCategory
    form_class = SubCategoryForm
    success_url = reverse_lazy('subcategory_list')

class SubCategoryDeleteView(BaseDeleteView):
    model = SubCategory
    success_url = reverse_lazy('subcategory_list')

