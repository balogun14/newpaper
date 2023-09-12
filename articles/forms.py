from django import forms

from .models import Comment


class CommentForm(forms.ModelForm):
    """
    docstring
    """

    class Meta:
        model = Comment
        fields = ("comment", "author")
