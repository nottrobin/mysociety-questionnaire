from django.db import models

class Constituency(models.Model):
    """ Database model for constituencies """

    name = models.CharField(max_length=200)

class Party(models.Model):
    """ Database model for political parties """

    name = models.CharField(max_length=200)
    abbreviation = models.CharField(max_length=10)

class AnswerSet(models.Model):
    """ Database model for sets of answers """

    VOTE_OPTIONS = (
        ('yes', "Yes"),
        ('no', "No"),
        ('undecided', "Undecided"),
    )

    constituency = models.ForeignKey(Constituency)
    going_to_vote = models.CharField(max_length=10, choices=VOTE_OPTIONS)
    voting_for = models.ForeignKey(Party, null=True)

