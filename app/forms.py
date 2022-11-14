from django.forms import ModelForm
from app.models import cliente


class clienteForm(ModelForm):
    class Meta:
        model = cliente 
        fields = ['login','senha','data_nascimento']

    
    