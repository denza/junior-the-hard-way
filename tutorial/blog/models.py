from django.db import models
from django.conf import settings

class Blog(models.Model):
    blog_title = models.CharField(max_length = 50)
    
    def __str__(self):
        return self.blog_title

class Post(models.Model):
    blog = models.ForeignKey(Blog, on_delete = models.CASCADE)
    post_title = models.CharField(max_length = 50)
    post_text = models.TextField()

    def __str__(self):
        return self.post_title