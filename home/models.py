import csv
from distutils.command import upload
from django.db import models
import sys


from home.calculation.analysis import *

# Create your models here.
class post(models.Model):
    """Model definition for post."""

    # TODO: Define fields here
    title = models.CharField(max_length=50, blank=True, null=True)
    content = models.CharField(max_length=200 , blank=True, null=True)

    class Meta:
        """Meta definition for post."""

        verbose_name = 'post'
        verbose_name_plural = 'posts'

    def __str__(self):
        """Unicode representation of post."""
        return self.title

class variant(models.Model):


    def __str__(self):
        """Unicode representation of post."""
        return self.variant_count
