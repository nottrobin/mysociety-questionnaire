from django.db import models

class Constituency(models.Model):
    """ Database model for constituencies """

    name = models.CharField(max_length=200)

class Party(models.Model):
    """ Database model for political parties """

    name = models.CharField(max_length=200)
    abbreviation = models.CharField(max_length=10)
 