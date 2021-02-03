from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['name', 'title', 'email', 'address', 'productType', 'productNum', 'bodyText', 'picture']

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class' : 'name'})       