from django import forms


class UserRegisterForm(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'first name'}))
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'last name'}))
    username = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'username'}))
    email = forms.EmailField(widget=forms.TextInput(
        attrs={'placeholder': 'email'}))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'placeholder': 'password'})
    )
