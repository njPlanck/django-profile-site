from django.db import models

# Create your models here.
class Project(models.Model):
  title = models.CharField(max_length=200)
  summary = models.TextField(max_length=600)
  description = models.TextField()
  link = models.CharField(max_length=600)
  category= models.CharField(max_length=100)
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)


  def __str__(self):
    return self.title