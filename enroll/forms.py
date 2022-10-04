from django import forms

class StudentRegistration(forms.Form):
    name = forms.CharField(max_length=70)
    email = forms.EmailField(max_length=100)
    password = forms.CharField(max_length=100 , widget=forms.PasswordInput)