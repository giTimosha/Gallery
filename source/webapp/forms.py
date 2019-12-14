from django import forms

from webapp.models import Photo


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['pictures', 'text', 'author_name']
