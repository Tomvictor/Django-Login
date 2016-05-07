from django import forms


class SignUpForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    email = forms.EmailField()
    gender_options = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others'),
    )
    Gender = forms.ChoiceField(widget=forms.Select, choices=gender_options)
    about= forms.CharField(widget=forms.Textarea,max_length=250)
    password = forms.CharField(widget=forms.PasswordInput)