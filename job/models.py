from django.db import models
from django.conf import settings
import datetime

class Job(models.Model):
	name = models.CharField(max_length=200)
	father_name = models.CharField(max_length=200)
	cnic = models.CharField(max_length=200)
	phone_no = models.IntegerField()
	email = models.CharField(max_length=200)
	experience = models.CharField(max_length=200, blank=True, null=True)
	address = models.CharField(max_length=200)
	current_city = models.CharField(max_length=200)
	date_time = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name