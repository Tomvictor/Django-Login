from django import forms


class SignUpForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=100)
    last_name = forms.CharField(label='Last Name', max_length=100)
    email = forms.EmailField()
    gender_options = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others'),
    )
    gender = forms.ChoiceField(label='Gender',widget=forms.Select, choices=gender_options)
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Enter your password',widget=forms.PasswordInput)
    about = forms.CharField(label='About you in 250 chars',widget=forms.Textarea, max_length=250)


class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Enter your password', widget=forms.PasswordInput)