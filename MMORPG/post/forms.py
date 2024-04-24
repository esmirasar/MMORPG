from django import forms
from .models import Post
from django_ckeditor_5.widgets import CKEditor5Widget


# Форма создания поста
class PostCreateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["text"].required = False

    text = forms.CharField(widget=CKEditor5Widget(config_name='extends'))

    class Meta:
        model = Post
        fields = [
            'title',
            'text',
            'category'
        ]


# Форма редактирования поста
class PostUpdateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["text"].required = False

    text = forms.CharField(widget=CKEditor5Widget(config_name='extends'))

    class Meta:
        model = Post
        fields = [
            'title',
            'text',
            'category'
        ]
