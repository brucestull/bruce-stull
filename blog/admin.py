from django.contrib import admin

from . import models


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Admin class for models.Category model.
    """
    list_display = (
        "name",
    )


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    """
    Admin class for models.Post model.
    """
    list_display = (
        "title",
    )


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Admin class for models.Comment model.
    """
    list_display = (
        "author",
        "post",
    )
