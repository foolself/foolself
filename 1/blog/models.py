from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    author=models.ForeignKey(User)
    title=models.CharField(max_length=200)
    text=models.TextField()
    def __unicode__(self):
        return self.title
    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = verbose_name

class UploadFile(models.Model):
	name = models.CharField(max_length=50)
	file = models.FileField(upload_to = "uploads/%Y/%m")

