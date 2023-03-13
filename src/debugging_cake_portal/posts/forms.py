from django import forms
from .models import Post


class UploadPost(forms.ModelForm):
    title = forms.CharField(max_length=50)
    description = forms.CharField(max_length=200)
    file = forms.FileField()
    filename = forms.CharField(max_length=100)

    class Meta:
        model = Post
        fields = ("title", "description", "post_tag", "file",)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"
