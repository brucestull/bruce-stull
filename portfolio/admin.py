from django.contrib import admin

from portfolio.models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = (
        "created_at",
        "updated_at",
    )
    list_display = (
        "title",
        "truncated_description",
        "technology",
        "image",
        "created_at",
    )

    def truncated_description(self, obj):
        """
        Truncate `description` to 30 characters.
        """
        return obj.description[:30]

