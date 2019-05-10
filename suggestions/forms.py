from django import forms
from .models import Suggestion


class ProductSuggestForm(forms.ModelForm):

    class Meta:
        model = Suggestion
        fields = ('title', 'content')