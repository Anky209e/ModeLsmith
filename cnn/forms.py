from .models import ImageModel
from django import forms

class ImageForm(forms.ModelForm):

    class Meta:
        model = ImageModel
        fields = ["image_field"]
