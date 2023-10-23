from django.db import models

class Place(models.Model):

  def __str__(self):
    return '%s' % (self.title)

  title = models.CharField(max_length=200)
  text = models.JSONField(max_length=1000, default='')

# Register your models here.
