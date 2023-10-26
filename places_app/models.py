from django.db import models
#from django.contrib.gis.db import models

class Place(models.Model):

  def __str__(self):
    return '%s' % (self.title)

  title = models.CharField(max_length=200)
  description_short = models.CharField(max_length=1000, default='')
  description_long = models.CharField(max_length=1000, default='')
  #coordinates = models.PolygonField()
  lng = models.FloatField(default=0)
  lat = models.FloatField(default=0)

