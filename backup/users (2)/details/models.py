from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Question(models.Model):
    month = models.IntegerField()
    date = models.IntegerField()
    my_order = models.PositiveIntegerField(default=0, blank=False, null=False)

    def __unicode__(self):
    	return str(self.month)


    class Meta(object):
        ordering = ('my_order',)


