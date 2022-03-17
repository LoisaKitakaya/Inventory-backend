from django import forms
from .models import InventoryItem

class AddItem(forms.ModelForm):

    class Meta:

        model = InventoryItem

        fields = '__all__'

        exclude = [
            'slug',
            'archived_on',
            'last_modified',
        ]