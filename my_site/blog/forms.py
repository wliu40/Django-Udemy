from django import forms
from .models import Comment


class CommentForm(forms.Form):
    class Meta:
        model = Comment
        fields = ['user_name', 'user_email', 'text'] # or exclude = ['post']
        widgets = {
            'user_name': forms.TextInput(attrs={'class': 'form-control'}),
            'user_email': forms.EmailInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control'})
        }
        labels = {
            'user_name': 'Your Name',
            'user_email': 'Your Email',
            'text': 'Your Comment'
        }