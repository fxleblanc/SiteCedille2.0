from django.test import TestCase
from member.models import Member


class MemberTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        member = Member.objects.create(
            firstname='Club', lastname='Cedille', status='A',
            biography="Club Cedille", title="Club"
        )

    def testFirstName(self):
        """A member must have a First Name"""
        member = Member.objects.get(firstname="Club")
        self.assertEqual(member.firstname, 'Club')

    def testLastName(self):
        """A member must have a Last Name"""
        member = Member.objects.get(firstname="Club")
        self.assertEqual(member.lastname, 'Cedille')

    def testStatus(self):
        """A member must have a status"""
        member = Member.objects.get(firstname="Club")
        self.assertEqual(member.status, 'A')

    def testBiography(self):
        """A member must have a biography"""
        member = Member.objects.get(firstname="Club")
        self.assertEqual(member.biography, "Club Cedille")

    def testTitle(self):
        """A member must have a title"""
        member = Member.objects.get(firstname="Club")
        self.assertEqual(member.title, "Club")
