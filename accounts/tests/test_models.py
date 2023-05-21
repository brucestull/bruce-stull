from django.test import TestCase
from django.db import models

from accounts.models import CustomUser

CUSTOM_USER_REGISTRATION_ACCEPTED_LABEL = "registration accepted"
CUSTOM_USER_REGISTRATION_ACCEPTED_HELP_TEXT = "Designates whether user's registration has been accepted by an admin."

A_TEST_USERNAME = 'ACustomUser'


class CustomUserModelTest(TestCase):
    """
    Tests for `CustomUser` model.
    """

    @classmethod
    def setUpTestData(cls):
        """
        Set up non-modified objects used by all test methods.

        This specific function name `setUpTestData` is required by Django.
        """
        user = CustomUser.objects.create(
            username=A_TEST_USERNAME,
        )

    def test_registration_accepted_label(self):
        """
        `CustomUser` model `registration_accepted` field label should be `registration accepted`.
        """
        user = CustomUser.objects.get(id=1)
        field_label = user._meta.get_field('registration_accepted').verbose_name
        self.assertEqual(field_label, CUSTOM_USER_REGISTRATION_ACCEPTED_LABEL)

    def test_registration_accepted_help_text(self):
        """
        `CustomUser` model `registration_accepted` field help text should be `Designates whether user's registration has been accepted by an admin.`.
        """
        user = CustomUser.objects.get(id=1)
        field_help_text = user._meta.get_field('registration_accepted').help_text
        self.assertEqual(field_help_text, CUSTOM_USER_REGISTRATION_ACCEPTED_HELP_TEXT)

    def test_registration_accepted_default_false(self):
        user = CustomUser.objects.get(id=1)
        field_default = user._meta.get_field('registration_accepted').default
        self.assertEqual(field_default, False)

    def test_dunder_string_method(self):
        """
        `CustomUser` model `__str__` method should return `username`.
        """
        user = CustomUser.objects.get(id=1)
        self.assertEqual(user.__str__(), user.username)
