from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):

	user = models.ForeignKey(User)
	question = models.TextField()

class LikeQuestion(models.Model):

	user = models.ForeignKey(User)
	question = models.ForeignKey(Question)
	like = models.BooleanField(default = False)