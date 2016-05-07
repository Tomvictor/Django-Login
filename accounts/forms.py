from django import forms


class SignUpForm(forms.Form):
    name = forms.CharField(label='name', max_length=100)
    email = forms.EmailField()
    about= forms.CharField(widget=forms.Textarea,max_length=250)
