from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """
    A CustomUser class is added so we can add functionality to `AbstractUser`.
    """

    registration_accepted = models.BooleanField(
        default=False,
        help_text="Designates whether user's registration has been accepted by an admin.",
    )

    def __str__(self):
        """
        String representation of CustomUser.
        """
        return self.username
