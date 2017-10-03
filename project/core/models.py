from django.db import models


class Post(models.Model):

	title = models.CharField(max_length=255)
	text = models.TextField(default='')




Post(title='111', text="sfefsrgsefefeffsef").save()
Post.objects.all()

