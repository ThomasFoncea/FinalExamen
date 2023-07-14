from django import forms
from .models import noticias



class NoticiaForm(forms.ModelForm):
    class Meta:
        model = noticias

        fields = '__all__'