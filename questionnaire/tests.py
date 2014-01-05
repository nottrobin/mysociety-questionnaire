from django.test import TestCase

from questionnaire.models import Constituency, Party, AnswerSet

class ConstituencyTests(TestCase):
    """ Test the Constituency model """

    def test_creation(self):
        """ Create constituency, save in database, retrieve """

        constituency = Constituency(name="Merthyr Tydfil and Rhymney")
        self.assertIsNone(constituency.id)
        constituency.save()
        self.assertIsNotNone(constituency.id)
        self.assertIs(type(constituency.id), int)

        constituency_again = Constituency.objects.get(id=constituency.id)
        self.assertEqual(constituency.name, constituency_again.name)

class PartyTests(TestCase):
    """ Tests for Party model """

    def test_creation(self):
        """ Create party, save, retrieve """

        party = Party(name="Plaid Cymru", abbreviation="PC")
        self.assertIsNone(party.id)
        party.save()
        self.assertIsNotNone(party.id)
        self.assertIs(type(party.id), int)

        party_again = Party.objects.get(id=party.id)
        self.assertEqual(party.name, party_again.name)
        self.assertEqual(party.abbreviation, party_again.abbreviation)

class AnswerSetTests(TestCase):
    """ Test the AnswerSet model """

    def test_creation(self):
        """ Create answerset """

        constituency = Constituency(name="Merthyr Tydfil and Rhymney")
        constituency.save()

        party = Party(name="Plaid Cymru", abbreviation="PC")
        party.save()

        answers = AnswerSet(
            constituency=constituency,
            going_to_vote="yes",
            voting_for=party
        )
        answers.save()
