from django import forms
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout,Submit
from library.models import Book

class AddBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = (
            'bname',
            'category',
            'author',
            'publisher',
            'price',
            'image',
            'download',
            'review'
        )

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

            self.helper = FormHelper
            self.helper.form_method = 'post'
            self.helper.layout = Layout(
                'bname',
                'category',
                'author',
                'publisher',
                'price',
                'image',
                'download',
                'review',


            Submit('submit', 'Submit', css_class='btn-success')
        )