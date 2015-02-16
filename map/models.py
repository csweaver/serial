from django.db import models

# Create your models here.
class Tower(models.Model):
	name = models.TextField()
	x = models.IntegerField()
	y = models.IntegerField()

	def __str__(self):
		return self.name
	

class Call(models.Model):
	name = models.TextField()
	time = models.DateTimeField()
	duration = models.IntegerField()
	tower = models.ForeignKey(Tower)
	
	def __str__(self):
		return self.name + " " + self.time.strftime('%Y-%m-%d %H:%M')
