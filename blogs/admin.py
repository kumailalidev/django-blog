from django.contrib import admin
from .models import Category, Blog


class BlogAdmin(admin.ModelAdmin):
    """Admin class for blog model."""

    prepopulated_fields = {
        "slug": ("title",),
    }


admin.site.register(Category)
admin.site.register(Blog, BlogAdmin)
