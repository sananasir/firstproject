from django.db import models
from django.utils import timezone

class Question(models.Model):
	question_text=models.CharField(max_length=200)
	pub_date=models.DateTimeField('date Published')


class Choice(models.Model):
	question=models.ForeignKey(Question, on_delete=models.CASCADE)
	choice_text=models.CharField(max_length=200)
	votes=models.IntegerField(default=0)


class Post(models.Model):
	author=models.ForeignKey('auth.user')
	title=models.CharField(max_length=200)
	text=models.TextField()
	created_date=models.DateTimeField(
		default=timezone.now)
	published_date=models.DateTimeField(
		blank=True, null=True)

	def publish(self):
		self.published_date=timezone.now()
		self.save()
	
	def __str__(self):
		return self.title

# Create your models here.
