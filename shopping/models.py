from django.db import models

# Create your models here.

class Vetement(models.Model):
    """
     Table representant des vetements
    """

    name = models.CharField(max_length=255)
    description = models