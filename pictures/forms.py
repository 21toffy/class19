form django import forms

from pictures.models import PictureAlbum


class PictureForm(forms.ModelForm):
    class meta:
        model = PictureAlbum
        fields = ('picture1', 'picture2', 'picture3', 'picture4', 'tag')