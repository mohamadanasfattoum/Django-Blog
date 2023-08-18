from django.db import models

# Create your models here.


class Post (models.Model):
    title= models.CharField(max_length=120)
    comment = models.TextField(max_length=5000)
    publish_date = models.TimeField()