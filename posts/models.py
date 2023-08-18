from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Post (models.Model):
    title= models.CharField(max_length=120)
    comment = models.TextField(max_length=5000)
    publish_date = models.DateTimeField()
    auther = models.ForeignKey(User,related_name='post_auther',on_delete=models.SET_NULL,null=True)


    def __str__(self) -> str:
        return self.title