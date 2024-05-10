from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['name', 'email', 'review'] # which fields to show in the form
        labels = {
            'name': 'Your Name',
            'email': 'Your Email',
            'review': 'Your Review'
        }
        error_messages  = {
            'name': {
                'required': 'Please enter your name:)',
                'max_length': 'Please enter a shorter name:)',
            },
            'email': {
                'required': 'Please enter your email:)',
                'max_length': 'Please enter a shorter email:)',
            }
        }

class myform(forms.Form):
    name = forms.CharField(label='Your Name', max_length=100, error_messages={'required': 'Please enter your name:)', 
                                                                              'max_length': 'Please enter a shorter name:)'})
    email = forms.EmailField(label='Your Email', max_length=100)
    review = forms.CharField(label='Your Review', widget=forms.Textarea(attrs={'rows': 5, 'cols': 20}))