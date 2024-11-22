from django.db import models
import uuid

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=500)
    artist = models.CharField(max_length=500, null=True)
    url = models.URLField(max_length=500, null=True)
    image = models.URLField(max_length=500)
    body = models.TextField()
    tags = models.ManyToManyField('Tag', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    id = models.CharField(max_length=100, primary_key=True, default=uuid.uuid4, editable=False)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created']
        
class Tag(models.Model):
    name = models.CharField(max_length=20)
    image = models.FileField(upload_to='icons/', null=True, blank=True)
    slug = models.SlugField(max_length=20, unique=True) # slugfield is the lowercase version of the name and without spaces
    order = models.IntegerField(null = True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['order'] # - for descending order and + for ascending order and created is the field name