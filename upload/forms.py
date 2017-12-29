from django import forms

from .models import Donor_List

class UploadForm(forms.ModelForm):
    class Meta:
        model = Donor_List
        fields = [
            'fileobj',
            'text',
        ]
        
