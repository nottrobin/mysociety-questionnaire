from django.test import TestCase

from questionnaire.models import Constituency

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
