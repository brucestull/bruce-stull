from django.test import TestCase

from portfolio.models import Project, Technology
from portfolio.admin import ProjectAdmin, TechnologyAdmin


class TestTechnologyAdmin(TestCase):
    """
    Test the `TechnologyAdmin` class.
    """

    def test_get_fieldsets_is_list_of_tuples(self):
        """
        `TechnologyAdmin` `get_fieldsets()` method should return a list of tuples.
        """
        technology_admin = TechnologyAdmin(Technology, None)
        fieldsets = technology_admin.get_fieldsets(request=None, obj=None)
        self.assertIsInstance(fieldsets, list)
        self.assertIsInstance(fieldsets[0], tuple)

    def test_get_fieldsets_has_name_in_first_element(self):
        """
        `TechnologyAdmin` `get_fieldsets()` method should return a list of tuples that includes `name`.
        """
        technology_admin = TechnologyAdmin(Technology, None)
        fieldsets = technology_admin.get_fieldsets(request=None, obj=None)
        fieldsets_as_list = list(fieldsets)
        self.assertIn("name", fieldsets_as_list[0][1]["fields"][0])

    def test_get_fieldsets_has_description_in_second_element(self):
        """
        `TechnologyAdmin` `get_fieldsets()` method should return a list of tuples that includes `description`.
        """
        technology_admin = TechnologyAdmin(Technology, None)
        fieldsets = technology_admin.get_fieldsets(request=None, obj=None)
        fieldsets_as_list = list(fieldsets)
        self.assertIn("description", fieldsets_as_list[0][1]["fields"][1])

    def test_get_fieldsets_has_created_at_in_third_element(self):
        """
        `TechnologyAdmin` `get_fieldsets()` method should return a list of tuples that includes `created_at`.
        """
        technology_admin = TechnologyAdmin(Technology, None)
        fieldsets = technology_admin.get_fieldsets(request=None, obj=None)
        fieldsets_as_list = list(fieldsets)
        self.assertIn("created_at", fieldsets_as_list[0][1]["fields"][2])


class TestProjectAdmin(TestCase):
    """
    Test the `ProjectAdmin` class.
    """

    def test_project_admin_truncated_description_method_returns_description(self):
        """
        `ProjectAdmin` `truncated_description()` method should return the `description`.
        """
        project_admin = ProjectAdmin(Project, None)
        project = Project.objects.create(
            title="Test Project",
            description="Test description",
            image="test.jpg",
        )
        self.assertEqual(
            project_admin.truncated_description(project),
            project.description,
        )

def test_project_admin_truncated_description_method_returns_truncated_description(self):
        """
        `ProjectAdmin` `truncated_description()` method should return the truncated `description`.
        """
        project_admin = ProjectAdmin(Project, None)
        project = Project.objects.create(
            title="Test Project",
            description="This is a description with more than 30 characters.",
            image="test.jpg",
        )
        truncated_description = "This is a description with more than 30 characters."[:30]
        self.assertEqual(
            project_admin.truncated_description(project),
            truncated_description,
        )
