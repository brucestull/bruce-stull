from django.test import TestCase

from accounts.models import CustomUser
from accounts.admin import CustomUserAdmin


TEST_USERNAME_ONE = 'ACustomUser'
TEST_PASSWORD_ONE = 'TEST_PASSWORD_ONE'
TEST_FIRST_NAME_ONE = 'A'

TEST_USERNAME_TWO = 'AnotherCustomUser'
TEST_PASSWORD_TWO = 'TEST_PASSWORD_TWO'
TEST_FIRST_NAME_TWO = 'Another'

class TestCustomUserAdmin(TestCase):
    @classmethod
    def setUpTestData(cls):
        """
        Set up non-modified objects used by all test methods.

        This specific function name `setUpTestData` is required by Django.
        """
        cls.user = CustomUser.objects.create(
            username=TEST_USERNAME_ONE,
            first_name=TEST_FIRST_NAME_ONE,
        )

    def test_get_fieldsets_is_list_of_tuples(self):
        """
        `CustomUserAdmin` `get_fieldsets()` method should return a list of tuples.
        """
        custom_user_admin = CustomUserAdmin(CustomUser, None)
        fieldsets = custom_user_admin.get_fieldsets(request=None, obj=None)
        self.assertIsInstance(fieldsets, list)
        self.assertIsInstance(fieldsets[0], tuple)

    def test_get_fieldsets_has_moderator_permissions_in_second_element(self):
        """
        `CustomUserAdmin` `get_fieldsets()` method should return a list of tuples that includes `Moderator Permissions`.
        """
        custom_user_admin = CustomUserAdmin(CustomUser, None)
        fieldsets = custom_user_admin.get_fieldsets(request=None, obj=None)
        fieldsets_as_list = list(fieldsets)
        self.assertIn("Moderator Permissions", fieldsets_as_list[1])

    def test_list_display_includes_username(self):
        """
        `CustomUserAdmin` `list_display` should include `username`.
        """
        custom_user_admin = CustomUserAdmin(CustomUser, None)
        self.assertIn("username", custom_user_admin.list_display)

    def test_list_display_includes_registration_accepted(self):
        """
        `CustomUserAdmin` `list_display` should include `registration_accepted`.
        """
        custom_user_admin = CustomUserAdmin(CustomUser, None)
        self.assertIn("registration_accepted", custom_user_admin.list_display)
