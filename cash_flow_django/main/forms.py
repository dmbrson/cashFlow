from django import forms
from django.utils.timezone import now
from .models import CashFlowRecord

class CashFlowRecordForm(forms.ModelForm):
    class Meta:
        model = CashFlowRecord
        fields = ['status', 'type', 'category', 'subcategory', 'amount', 'comment', 'created_at']