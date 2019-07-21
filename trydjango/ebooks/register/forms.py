
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout,Submit
from django import forms
from .models import UserProfileInfo
from django.conf import settings
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())

	class Meta():
		model = User
		fields = ('first_name','last_name','username','password','email')
class UserProfileInfoForm(forms.ModelForm):
	class Meta():
		model = UserProfileInfo
		fields = ('mobile',)

		def __init__(self, *args, **kwargs):
			super().__init__(*args, **kwargs)

			self.helper = FormHelper
			self.helper.form_method = 'post'
			self.helper.layout = Layout(
				'First name',
				'Last name',
				'Username',
				'Password',
				'Email address',
				'Mobile',


				Submit('submit', 'Submit', css_class='btn-success')
			)