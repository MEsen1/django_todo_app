from django import forms
from .models import Todo

#? forms.Form and forms.ModelForm
class TodoForm(forms.ModelForm):
    
    class Meta:
        model=Todo
        fields ='__all__'
    
    
    


