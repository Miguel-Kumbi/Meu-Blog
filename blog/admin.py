from django.contrib import admin
from .models import Category, Tag, Post


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	list_display = ("name", "slug")
	search_fields = ("name",)
	ordering = ("name",)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
	list_display = ("name", "slug")
	search_fields = ("name",)
	ordering = ("name",)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	list_display = (
		"title",
		"author",
		"category",
		"created_at",
		"published_at",
	)

	list_filter = (
		"category",
		"tags",
		"published_at",
	)

	search_fields = (
		"title",
		"content",
	)

	prepopulated_fields = {
		"slug": ("title",)
	}

	ordering = (
		"-created_at",
	)

	fields = (
		"title",
		"slug",
		"content",
		"author",
		"category",
		"tags",
		"published_at",
	)
