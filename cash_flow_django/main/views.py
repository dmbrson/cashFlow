from django.shortcuts import render, redirect
from main.forms import CashFlowRecordForm
from main.models import CashFlowRecord, SubCategory, Category
from django.http import JsonResponse

#Главная страница: список записей
def record_list(request):
    records = CashFlowRecord.objects.all()
    return render(request, 'main/record_list.html', {
        'records': records,
    })

# Создание записи
def record_create(request):
    if request.method == 'POST':
        form = CashFlowRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('record_list')
    else:
        form = CashFlowRecordForm()
    return render(request, 'main/record_form.html', {'form': form})

# Получение подкатегории
def get_subcategories(request):
    category_id = request.GET.get('category_id')
    subcategories = SubCategory.objects.filter(category_id=category_id)
    subcategories_data = list(subcategories.values('id', 'name'))
    return JsonResponse({'subcategories': subcategories_data})