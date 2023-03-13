from django import forms
from .models import Comment
from django.db.migrations.state import get_related_models_tuples
from django.utils.translation import gettext_lazy as _


class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'md-textarea form-control',
        'placeholder': 'comment here ...',
        'rows': '4',
        'label': 'Comment'
    }))

    class Meta:
        model = Comment
        fields = ('content', 'parent',)

        labels = {
            'content': _(''),
        }

        widgets = {
            'content': forms.TextInput(),
        }
