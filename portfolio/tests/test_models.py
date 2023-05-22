from django.test import TestCase

from portfolio.models import Project

PROJECT_TITLE_LABEL = "title"
PROJECT_TITLE_MAX_LENGTH = 100
PROJECT_TITLE = "Test Project"

PROJECT_DESCRIPTION_LABEL = "description"
PROJECT_DESCRIPTION_HELP_TEXT = "Enter a description of the project."
PROJECT_DESCRIPTION = "Test description."

PROJECT_TECHNOLOGY_LABEL = "technology"
PROJECT_TECHNOLOGY_HELP_TEXT = "Enter the technology used in the project."
PROJECT_TECHNOLOGY_MAX_LENGTH = 30
PROJECT_TECHNOLOGY = "Django"

PROJECT_IMAGE_LABEL = "image"
PROJECT_IMAGE_HELP_TEXT = "Add an image of the project."
PROJECT_IMAGE_PATH = "/img"
PROJECT_IMAGE = "test_image.jpg"


class ProjectTest(TestCase):
    """
    Tests for `Project` model.
    """

    @classmethod
    def setUpTestData(cls):
        """
        Set up non-modified objects used by all test methods.

        This specific function name `setUpTestData` is required by Django.
        """
        cls.project = Project.objects.create(
            title=PROJECT_TITLE,
            description=PROJECT_DESCRIPTION,
            technology=PROJECT_TECHNOLOGY,
            image=PROJECT_IMAGE,
        )

    def test_title_label(self):
        """
        `Project` model `title` field label should be `title`.
        """
        field_label = self.project._meta.get_field(PROJECT_TITLE_LABEL).verbose_name
        self.assertEqual(field_label, PROJECT_TITLE_LABEL)

    def test_title_max_length(self):
        """
        `Project` model `title` field max length should be 100.
        """
        max_length = self.project._meta.get_field(PROJECT_TITLE_LABEL).max_length
        self.assertEqual(max_length, PROJECT_TITLE_MAX_LENGTH)

    def test_description_label(self):
        """
        `Project` model `description` field label should be `description`.
        """
        field_label = self.project._meta.get_field(
            PROJECT_DESCRIPTION_LABEL
        ).verbose_name
        self.assertEqual(field_label, PROJECT_DESCRIPTION_LABEL)

    def test_description_help_text(self):
        """
        `Project` model `description` field help text should be `Enter a description of the project.`.
        """
        help_text = self.project._meta.get_field(PROJECT_DESCRIPTION_LABEL).help_text
        self.assertEqual(help_text, PROJECT_DESCRIPTION_HELP_TEXT)

    def test_technology_label(self):
        """
        `Project` model `technology` field label should be `technology`.
        """
        field_label = self.project._meta.get_field(
            PROJECT_TECHNOLOGY_LABEL
        ).verbose_name
        self.assertEqual(field_label, PROJECT_TECHNOLOGY_LABEL)

    def test_technology_help_text(self):
        """
        `Project` model `technology` field help text should be `Enter the technology used in the project.`.
        """
        help_text = self.project._meta.get_field(PROJECT_TECHNOLOGY_LABEL).help_text
        self.assertEqual(help_text, PROJECT_TECHNOLOGY_HELP_TEXT)

    def test_technology_max_length(self):
        """
        `Project` model `technology` field max length should be 30.
        """
        max_length = self.project._meta.get_field(PROJECT_TECHNOLOGY_LABEL).max_length
        self.assertEqual(max_length, PROJECT_TECHNOLOGY_MAX_LENGTH)

    def test_image_label(self):
        """
        `Project` model `image` field label should be `image`.
        """
        field_label = self.project._meta.get_field(PROJECT_IMAGE_LABEL).verbose_name
        self.assertEqual(field_label, PROJECT_IMAGE_LABEL)

    def test_image_help_text(self):
        """
        `Project` model `image` field help text should be `Add an image of the project.`.
        """
        help_text = self.project._meta.get_field(PROJECT_IMAGE_LABEL).help_text
        self.assertEqual(help_text, PROJECT_IMAGE_HELP_TEXT)

    def test_image_path(self):
        """
        `Project` model `image` field path should be `/img`.
        """
        path = self.project._meta.get_field(PROJECT_IMAGE_LABEL).path
        self.assertEqual(path, PROJECT_IMAGE_PATH)

    def test_created_at_label(self):
        """
        `Project` model `created_at` field label should be `created at`.
        """
        field_label = self.project._meta.get_field("created_at").verbose_name
        self.assertEqual(field_label, "created at")

    def test_created_at_auto_now_add_attribute_true(self):
        """
        `Project` model `created_at` field should have `auto_now_add=True`.
        """
        auto_now_add = self.project._meta.get_field("created_at").auto_now_add
        self.assertTrue(auto_now_add)

    def test_updated_at_label(self):
        """
        `Project` model `updated_at` field label should be `updated at`.
        """
        field_label = self.project._meta.get_field("updated_at").verbose_name
        self.assertEqual(field_label, "updated at")

    def test_updated_at_auto_now_attribute_true(self):
        """
        `Project` model `updated_at` field should have `auto_now=True`.
        """
        auto_now = self.project._meta.get_field("updated_at").auto_now
        self.assertTrue(auto_now)

    def test_dunder_string_method(self):
        """
        `Project` model `__str__` method should return `title`.
        """
        self.assertEqual(self.project.__str__(), PROJECT_TITLE)
