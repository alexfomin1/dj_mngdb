from djongo import *

# Create your models here.
class Student(models.Model):
	name = models.CharField(max_length=50)
	fav_sport = models.TextField(max_length=300)

	def __str__(self):
		return self.name