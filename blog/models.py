from django.db import models
from django.dispatch import receiver
from django.db.models.signals import pre_delete

from accounts.models import CustomUser


class TimestampMixin(models.Model):
    """
    Abstract base class with a created_at and updated_at field.
    """

    created_at = models.DateTimeField(
        help_text="The date and time this object was created.",
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        help_text="The date and time this object was last updated.",
        auto_now=True,
    )

    class Meta:
        abstract = True


class Category(TimestampMixin, models.Model):
    """
    Model for a blog post category.
    """
    name = models.CharField(
        help_text="The name of the category.",
        max_length=20,
    )

    def __str__(self):
        """
        String representation of `Category`.
        """
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


class Post(TimestampMixin, models.Model):
    title = models.CharField(
        help_text="The title of the post.",
        max_length=255,
    )
    body = models.TextField(
        help_text="The text body of the post.",
    )
    categories = models.ManyToManyField(
        Category,
        help_text="The categories related to this post.",
        related_name="posts",
    )

    def __str__(self):
        """
        String representation of `Post`.
        """
        return self.title

class Comment(TimestampMixin, models.Model):
    author = models.ForeignKey(
        CustomUser,
        help_text="The name of the author of the comment.",
        max_length=60,
        on_delete=models.SET_NULL,
        null=True,
        related_name="comments",
    )
    body = models.TextField(
        help_text="The text body of the comment.",
    )
    post = models.ForeignKey(
        Post,
        help_text="The post this comment belongs to.",
        related_name="comments",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        """
        String representation of `Comment`.
        """
        return f"{self.author} on {self.post}"

@receiver(pre_delete, sender=CustomUser)
def set_author_deleted(sender, instance, **kwargs):
    Comment.objects.filter(author=instance).update(author='Author Deleted')