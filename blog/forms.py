from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    """Формы комментариев"""
    class Meta:
        model = Comment
        fields = ("text", )
