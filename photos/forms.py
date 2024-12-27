from django import forms

from photos.models import Photo


class PhotoBaseForm(forms.ModelForm):
    class Meta:
        model = Photo
        exclude = ['user']

class PhotoCreateForm(PhotoBaseForm):
    pass

class PhotoEditForm(forms.ModelForm):
    class Meta:
        model = Photo
        exclude = ['photo']

class PhotoDeleteForm(PhotoBaseForm):
    pass