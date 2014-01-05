from django.test import TestCase

from questionnaire.models import Constituency, Party

class ConstituencyTests(TestCase):
    """ Test the Constituency model """

    def test_creation(self):
        """ Create constituency, save in database, retrieve """

        name = "Merthyr Tydfil and Rhymney"
        constituency = Constituency(name=name)
        self.assertIsNone(constituency.id)
        constituency.save()
        self.assertIsNotNone(constituency.id)
        self.assertIs(type(constituency.id), int)

        constituency_again = Constituency.objects.get(id=constituency.id)
        self.assertEqual(name, constituency_again.name)

class PartyTests(TestCase):
    """ Tests for Party model """

    def test_creation(self):
        """ Create party, save, retrieve """

        name = "Plaid Cymru"
        abbreviation = "PC"

        party = Party(name=name, abbreviation=abbreviation)
        self.assertIsNone(party.id)
        party.save()
        self.assertIsNotNone(party.id)
        self.assertIs(type(party.id), int)

        party_again = Party.objects.get(id=party.id)
        self.assertEqual(name, party_again.name)
        self.assertEqual(abbreviation, party_again.abbreviation)
