from django import forms

from blog.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        default_attributes = {
            'class': 'form-control'
        }
        model = Post
        fields = ('heading', 'body', 'cover', 'status', 'category', )
        exclude = ('user', )
        widgets = {
            'heading': forms.TextInput(attrs=default_attributes),
            'body': forms.Textarea(attrs=default_attributes),
            # 'cover': forms.FileInput(attrs=default_attributes),
            'status': forms.widgets.Select(attrs=default_attributes),
            'category': forms.widgets.SelectMultiple(attrs=default_attributes),
        }
