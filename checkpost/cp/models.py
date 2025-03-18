from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    text = models.CharField(max_length=255, null=True)
    img = models.CharField(max_length=255, null= True)

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text_com = models.CharField(max_length=255)
    number_post = models.ForeignKey(Post, on_delete=models.CASCADE)