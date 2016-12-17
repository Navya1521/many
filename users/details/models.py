from __future__ import unicode_literals

from django.db import models


class Author(models.Model):
  name = models.CharField(max_length = 100)
  my_order = models.PositiveIntegerField(default=0, blank=False, null=False)

  def __unicode__(self):
    return str(self.name)


  class Meta(object):
    ordering = ('my_order',)

class Book(models.Model):
  title = models.CharField(max_length = 100)
  authors = models.ManyToManyField(Author, blank = False)

  my_order = models.PositiveIntegerField(default=0, blank=False, null=False)

  def __unicode__(self):
    return str(self.title)


  class Meta(object):
    ordering = ('title',)

# class Membership(models.Model):
#   author = models.ForeignKey(Author,on_delete = models.CASCADE)
#   book = models.ForeignKey(Book,on_delete = models.CASCADE)
#   date = models.DateField()
  

# Create your models here.


# class User(models.Model):
# 	fname = models.CharField(max_length = 100)
# 	lname = models.CharField(max_length = 100)

# 	my_order = models.PositiveIntegerField(default=0, blank=False, null=False)

# 	def __unicode__(self):
#    		return str(self.fname)

#   class Meta(object):
#    		ordering = ('my_order',)
# class Question(models.Model):
#     month = models.IntegerField()
#     date = models.IntegerField()
#     person = models.ManyToManyField(User,related_name = 'person_asking',through='Person')
#     my_order = models.PositiveIntegerField(default=0, blank=False, null=False)

#     def __unicode__(self):
#     	return str(self.month)

# 	class Meta(object):
# 		ordering = ('my_order',)

# class Person(models.Model):
#     person = models.ForeignKey(User)
#     question  = models.ForeignKey(Question)


