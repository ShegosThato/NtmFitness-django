from django import forms
from .models import Comment, Post
from django.contrib.auth import get_user_model


class CommentForm(forms.ModelForm):
    author = forms.ModelChoiceField(widget=forms.HiddenInput(
    ), queryset=get_user_model().objects.all(), disabled=True)
    post = forms.ModelChoiceField(
        widget=forms.HiddenInput(), queryset=Post.objects.all(), disabled=True)
    body = forms.TextInput()

    class Meta:
        model = Comment
        fields = ['body', 'author', 'post']
