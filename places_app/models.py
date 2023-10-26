import uuid

from django.db import models
#from django.contrib.gis.db import models

class Images(models.Model):
  def __str__(self):
    return '%s %s' % (self.indifer, self.place)
  LIST_NUMBER = (['1', '1'], ['2', '2'])
  indifer = models.CharField(choices=LIST_NUMBER, max_length=1)
  place = models.ForeignKey('Place', on_delete=models.SET_NULL, null=True)
  image = models.ImageField(unique=True)

  class Meta:
    unique_together = ('indifer', 'place')
class Place(models.Model):

  def __str__(self):
    return '%s' % (self.title)

  title = models.CharField(max_length=200)
  description_short = models.CharField(max_length=1000, default='')
  description_long = models.CharField(max_length=1000, default='')
  #coordinates = models.PolygonField()
  lng = models.FloatField(default=0)
  lat = models.FloatField(default=0)

