from django import forms
from django.utils.timezone import now
from .models import CashFlowRecord

class CashFlowRecordForm(forms.ModelForm):
    class Meta:
        model = CashFlowRecord
        fields = ['status', 'type', 'category', 'subcategory', 'amount', 'comment', 'created_at']

        widgets = {
            'status': forms.Select(attrs={
                'class': 'form-select',
                'placeholder': 'Статус'
            }),
            'type': forms.Select(attrs={
                'class': 'form-select',
                'placeholder': 'Тип'
            }),
            'category': forms.Select(attrs={
                'class': 'form-select',
                'placeholder': 'Категория'
            }),
            'subcategory': forms.Select(attrs={
                'class': 'form-select',
                'placeholder': 'Подкатегория'
            }),
            'amount': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Сумма'
            }),
            'comment': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Комментарий'
            }),
            'created_at': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control',
                'value': now().date()
            }),
        }