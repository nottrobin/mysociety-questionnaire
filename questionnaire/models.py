from django.db import models

class Constituency(models.Model):
    """ Database model for constituencies """

    name = models.CharField(max_length=200)
