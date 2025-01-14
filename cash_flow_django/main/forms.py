from django import forms
from django.utils.timezone import now
from .models import *

class RecordFilterForm(forms.Form):
    start_date = forms.DateField(
        required=False,
        label="Дата от",
        widget=forms.DateInput(attrs={
            'type': 'date',
            'class': 'form-control'}),
    )
    end_date = forms.DateField(
        required=False,
        label="Дата до",
        widget=forms.DateInput(attrs={
            'type': 'date',
            'class': 'form-control'}),

    )
    status = forms.ModelChoiceField(
        queryset=Status.objects.all(),
        required=False,
        label="Статус",
        widget=forms.Select(attrs={
            'class': 'form-select'
        }),

    )
    type = forms.ModelChoiceField(
        queryset=Type.objects.all(),
        required=False,
        label="Тип",
        widget=forms.Select(attrs={
            'class': 'form-select'
        }),

    )
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        required=False,
        label="Категория",
        widget=forms.Select(attrs={
            'class': 'form-select'
        }),

    )
    subcategory = forms.ModelChoiceField(
        queryset=SubCategory.objects.all(),
        required=False,
        label="Подкатегория",
        widget=forms.Select(attrs={
            'class': 'form-select'
        }),

    )

class CashFlowRecordForm(forms.ModelForm):
    class Meta:
        model = CashFlowRecord
        fields = ['status', 'type', 'category', 'subcategory', 'amount', 'comment', 'created_at']

        widgets = {
            'status': forms.Select(attrs={
                'class': 'form-select',
            }),
            'type': forms.Select(attrs={
                'class': 'form-select',
            }),
            'category': forms.Select(attrs={
                'class': 'form-select',
            }),
            'subcategory': forms.Select(attrs={
                'class': 'form-select',
            }),
            'amount': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '1000'
            }),
            'comment': forms.Textarea(attrs={
                'class': 'form-control',
            }),
            'created_at': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control',
            }, format='%Y-%m-%d'),
        }

    # Метод устанавливающий текущую дату при создании новой формы
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.instance.pk:
            self.fields['created_at'].initial = now().strftime('%Y-%m-%d')