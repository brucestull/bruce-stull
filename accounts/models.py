from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """
    A `CustomUser` class is created by inheriting from `AbstractUser`.
    We can then add new fields to the ones provided by `AbstractUser`.
    """

    registration_accepted = models.BooleanField(
        default=False,
        help_text="Designates whether user's registration has been accepted by an admin.",
    )

    # def delete(self, *args, **kwargs):
    #     """
    #     Set the author of comments to `Deleted User` when deleting a `CustomUser`.
    #     """
    #     self.comment_set.update(author="Deleted User")
    #     super().delete(*args, **kwargs)

    def __str__(self):
        """
        String representation of `CustomUser`.
        """
        return self.username
