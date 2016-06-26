from django.db import models


#for upload dates
from django.utils import timezone
import datetime

# Create your models here.
"""SUBJECT_CHOICE=(
	(1,'Physics'),
	(2,'Chemistry'),
	(3,'Projects'))
"""
class Subjects(models.Model):
	"""
		Stores the subject data
	"""
	subject = models.CharField(max_length=30)
	image = models.FileField(upload_to = 'uploads/',blank=True)

	def __str__(self):
		return self.subject


	#subject_name = models.CharField()

class Explain(models.Model):
	sub = models.ForeignKey(Subjects, on_delete=models.CASCADE)	
	topics = models.CharField(max_length=100)
	theory = models.TextField()
	details = models.TextField()
	image = models.FileField(upload_to = 'uploads/',blank=True)
	
	def __str__(self):
		return self.topics
