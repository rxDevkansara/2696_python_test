from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import TextInput, EmailInput, PasswordInput
from django.contrib.auth.forms import AuthenticationForm, UsernameField

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")
		widgets = {
					'username': TextInput(attrs={
						'class': 'form-control',
						'placeholder': 'Name'
						}),
					'email': EmailInput(attrs={'class': 'form-control'}),
					'password1': PasswordInput(attrs={'class': 'form-control'}),
					'password2': PasswordInput(attrs={'class': 'form-control'})
				}
	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = UsernameField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': '', 'name': 'username'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
	    	'name': 'password'
        }
))