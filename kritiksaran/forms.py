from django import forms
from.models import KritikSaran

class FormKritikSaran(forms.ModelForm):
    class Meta:
        model = KritikSaran
        fields = [
            'isi',
        ]

        labels = {
        	'isi' : 'Isi',
        }

        widgets = {
            'isi': forms.Textarea(
                attrs = {
                    'class':'form-control',
            	}
        	),
        }