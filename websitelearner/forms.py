from django import forms

class usersform(forms.Form):
    num1 = forms.CharField(label='Value 1', required=True, widget=forms.TextInput(attrs={'class':"form-control"}))
    num2 = forms.CharField(label='Value 2',  required=True, widget=forms.TextInput(attrs={'class':"form-control"}))
