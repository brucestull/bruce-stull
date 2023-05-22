from django.db import models


class Project(models.Model):
    """
    A Project class is created to store information about a project.
    """

    title = models.CharField(
        max_length=100,
    )
    description = models.TextField(
        help_text="Enter a description of the project.",
    )
    technology = models.CharField(
        help_text="Enter the technology used in the project.",
        max_length=30,
    )
    image = models.FilePathField(
        help_text="Add an image of the project.",
        path="static\images",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        """
        String representation of Project.
        """
        return self.title
