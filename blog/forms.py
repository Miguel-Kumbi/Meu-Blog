from django import forms
from .models import Post


class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = [
			'title',
			'slug',
			'content',
			'category',
			'tags'
		]

		def clean_title(self):
			title = self.cleaned_data['title']

			if not title.strip():
				raise forms.ValidationError('O título não pode estar vazio.')

			return title.strip()

		def clean_content(self):
			content = self.cleaned_data['content']

			if not content.strip():
				raise forms.ValidationError('O conteúdo não pode estar vazio.')

			return content.strip()