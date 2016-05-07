from django import forms


class SignUpForm(forms.Form):
    first_name = forms.CharField(label='first name', max_length=100)
    last_name = forms.CharField(label='first name', max_length=100)
    username = forms.CharField(label='first name', max_length=100)
    email = forms.EmailField()
    about= forms.CharField(widget=forms.Textarea,max_length=250)

