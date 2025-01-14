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