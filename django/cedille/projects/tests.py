from django.test import TestCase
from projects.models import Project


class PartnerTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        project = Project.objects.create(
            name="ClubCedille", description="123456", github="123456",
            status="A"
        )

    def testProjectName(self):
        """Test a project name"""
        project = Project.objects.get(name="ClubCedille")
        self.assertEqual(project.name, "ClubCedille")

    def testProjectDescription(self):
        """Test a project description"""
        project = Project.objects.get(name="ClubCedille")
        self.assertEqual(project.description, "123456")

    def testProjectGithub(self):
        """Test a project github"""
        project = Project.objects.get(name="ClubCedille")
        self.assertEqual(project.github, "123456")

    def testProjectStatus(self):
        """Test a project Status"""
        project = Project.objects.get(name="ClubCedille")
        self.assertEqual(project.status, "A")
