from django import forms
from django.forms import ImageField


class UploadedImageForm(forms.Form):
    image = ImageField(max_length=256)
