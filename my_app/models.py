from django.db import models

# Create your models here.
class Author(models.Model):
    full_name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.full_name


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    







