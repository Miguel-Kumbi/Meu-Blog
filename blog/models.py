from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
	name = models.CharField(
		max_length=100,
		unique=True # Evita duplicacão
	)
	slug = models.SlugField(
		max_length=100, 
		unique=True
	)

	class Meta:
		verbose_name_plural = "Categories"

	def __str__(self):
		return self.name


class Tag(models.Model):
	name = models.CharField(
		max_length=100,
		unique=True
	)
	slug = models.SlugField(
		max_length=100,
		unique=True
	)

	def __str__(self):
		return self.name


class Post(models.Model):
	title = models.CharField(
		max_length=200
	)
	slug = models.SlugField(
		max_length=100, 
		unique=True
	)
	content = models.TextField()
	author = models.ForeignKey(
		User,
		on_delete=models.SET_NULL, # Se um usuário for apagado deixara todos os posts relacionados a ele com NULL.
		null=True, # Valor NULL quando nenhum valor é preenchido.
		blank=True # Permite que o usuário envie o formulário sem preencher o campo.
	)
	category = models.ForeignKey(
		Category,
		on_delete=models.PROTECT # Impede que uma categoria seja apagada desde que tenham posts relacionados a ele.
	)
	tags = models.ManyToManyField(
		Tag,
		blank=True
	)
	created_at = models.DateTimeField(
		auto_now_add=True # Salvo automaticamente quando criado (Uma vez).
	)
	updated_at = models.DateTimeField(
		auto_now=True # Salvo automaticamente quando atualizado (varias vezes).
	)
	published_at = models.DateTimeField(
		null=True,
		blank=True
	)

	def __str__(self):
		return self.title