from django.shortcuts import render

from main.models import CashFlowRecord


#Главная страница: список записей
def record_list(request):
    records = CashFlowRecord.objects.all()
    return render(request, 'main/record_list.html', {
        'records': records,
    })