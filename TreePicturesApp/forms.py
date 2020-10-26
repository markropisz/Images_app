from django import forms
from .models import TreePicture

class TreePictureForm(forms.ModelForm):
    class Meta:
        model = TreePicture
        fields = '__all__'

