from __future__ import unicode_literals

from django.db import models


class FibonacciResults(models.Model):

    digits = models.IntegerField()
    final = models.IntegerField()
    time = models.CharField(max_length=255)

    class Meta:
        db_table = 'fibonacci_db'

    def __unicode__(self):
        return self.number
