from django import forms
from .models import Review
from django.forms import ModelForm

# class ReviewForm(forms.Form):
# 	first_name = forms.CharField(label='First Name', max_length=100)
# 	last_name = forms.CharField(label='Last Name', max_length=100)
# 	email = forms.EmailField(label='Email', max_length=100)
# 	review = forms.CharField(label='Please write your review here', max_length=500, widget=forms.Textarea(attrs={'class':'myform',
# 																											  'rows':'2', 'cols':'2'}))

class ReviewForm(ModelForm):
	class Meta:
		model = Review
		fields = "__all__"

		labels = {
			'first_name': 'Your First Name',
			'last_name': 'Your Last Name',
			'stars': 'Rating',
		}
