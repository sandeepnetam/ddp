
from django.forms import ModelForm
from .models import *


class DdpModelForm(ModelForm):
    class Meta:
        model = ddp
        fields = '__all__'
        widgets = {
            # 'name' : forms.TextInput(attrs={'class':'name form-control'} )
        }