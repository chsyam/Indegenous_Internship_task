from django.forms import ModelForm
from .models import Login

class DataCollection(ModelForm):
    class Meta:
        model = Login
        fields = '__all__'
