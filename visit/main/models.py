from __future__ import unicode_literals

from django.db import models

class Nutritionist(models.Model):
    title = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    fullname = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Meetings(models.Model):
    hourBegin = models.CharField(max_length=255)
    hourEnd = models.CharField(max_length=255)
    day = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    fullname = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    nutritionist = models.ForeignKey('Nutritionist',
                                     on_delete=models.CASCADE,
                                     )
    def __str__(self):
        return self.email