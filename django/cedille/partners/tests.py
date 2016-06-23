from django.test import TestCase
from partners.models import Partner


class PartnersTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        partner = Partner.objects.create(
            partnername="Cedille",
            website="cedille.club",
            status="True",
            ranking="G"
        )

    def testPartnerName(self):
        partner = Partner.objects.get(partnername="Cedille")
        self.assertEqual(partner.partnername, "Cedille")

    def testWebsiteName(self):
        partner = Partner.objects.get(partnername="Cedille")
        self.assertEqual(partner.website, "cedille.club")

    def testStatus(self):
        partner = Partner.objects.get(partnername="Cedille")
        self.assertEqual(partner.status, True)

    def testRanking(self):
        partner = Partner.objects.get(partnername="Cedille")
        self.assertEqual(partner.ranking, "G")
