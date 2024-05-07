from django import forms


class myform(forms.Form):
    name = forms.CharField(label='Your Name', max_length=100)
    email = forms.EmailField(label='Your Email', max_length=100)
    review = forms.CharField(label='Your Review', widget=forms.Textarea(attrs={'rows': 5, 'cols': 20}))