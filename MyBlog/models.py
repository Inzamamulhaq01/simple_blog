from typing import Iterable
from django.db import models
from django.utils.text import slugify

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    img = models.URLField(null = True)
    created_at = models.DateTimeField(auto_now_add = True)
    slug = models.SlugField(unique=True)


    def save (self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.title

class about(models.Model):
    content = models.TextField()
    
    
