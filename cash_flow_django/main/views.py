from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from main.forms import CashFlowRecordForm, RecordFilterForm
from main.models import CashFlowRecord, SubCategory, Category

#Главная страница: список записей
def record_list(request):
    records = CashFlowRecord.objects.all()
    filter_form = RecordFilterForm(request.GET)

    if filter_form.is_valid():
        start_date = filter_form.cleaned_data.get('start_date')
        end_date = filter_form.cleaned_data.get('end_date')
        status = filter_form.cleaned_data.get('status')
        type = filter_form.cleaned_data.get('type')
        category = filter_form.cleaned_data.get('category')
        subcategory = filter_form.cleaned_data.get('subcategory')

        if start_date:
            records = records.filter(created_at__gte=start_date)
        if end_date:
            records = records.filter(created_at__lte=end_date)
        if status:
            records = records.filter(status=status)
        if type:
            records = records.filter(type=type)
        if category:
            records = records.filter(category=category)
        if subcategory:
            records = records.filter(subcategory=subcategory)

    return render(request, 'main/record_list.html', {
        'records': records,
        'filter_form': filter_form,
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

# Получение категории
def get_categories(request):
    type_id = request.GET.get('type_id')
    categories = Category.objects.filter(type_id=type_id)
    categories_data = list(categories.values('id', 'name'))
    return JsonResponse({'categories': categories_data})

# Редактирование записи
def record_update(request, pk):
    record = get_object_or_404(CashFlowRecord, pk=pk)
    if request.method == 'POST':
        form = CashFlowRecordForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect('record_list')
    else:
        form = CashFlowRecordForm(instance=record)
    return render(request, 'main/record_form.html', {
        'form': form,
    })
def record_delete(request, pk):
    record = get_object_or_404(CashFlowRecord, pk=pk)
    if request.method == 'POST':
        record.delete()
        return redirect('record_list')
    return render(request, 'main/record_confirm_delete.html', {'record': record})