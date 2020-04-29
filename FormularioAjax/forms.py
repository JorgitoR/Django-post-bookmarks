from django import forms

from .models import Post

class PostForm(forms.ModelForm):

	class Meta:
		model = Post
		fields = ["texto"]

		widgets = {

			'texto':forms.TextInput(

				attrs = {'id':'post-formulario', 'requerid':True, 'placeholder':'Escribe tu post'}

				)

		}