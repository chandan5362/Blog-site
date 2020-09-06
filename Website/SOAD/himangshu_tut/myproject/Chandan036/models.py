from django.db import models

# Create your models here.
class Abhisarga(models.Model):

	eventName = models.CharField('Name',max_length = 25)
	eventdate = models.DateTimeField('EventDate')
	cordinator = models.CharField(max_length =25)
	venue = models.CharField(max_length= 25)
	eventtype = models.CharField(max_length =55)
	max_num_participants = models.IntegerField()
	event_rule = models.TextField(blank= True)
	event_prize = models.TextField(blank = True)


	def __str__(self):
		return self.eventName

