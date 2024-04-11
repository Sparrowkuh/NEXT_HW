from django.db import models

# Create your models here.
class Post(models.Model):
   title = models.CharField(max_length=50)
   content = models.TextField()


   def __str__(self):
       return self.title

class Comment(models.Model):
   post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
   content = models.TextField()


   def __str__(self):
       return self.content
