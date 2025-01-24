
from django.db import models
from django.contrib.admin import display
from django.utils.html import format_html
from django.urls import reverse


class Team(models.Model):
    image=models.ImageField()
    name=models.CharField(max_length=30)
    description=models.TextField()
    about=models.TextField()
    linkedin=models.CharField(max_length=100)
    facebook=models.CharField(max_length=100)
    instagram=models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    
    
class Blog(models.Model):
    title=models.CharField(max_length=50)
    description=models.TextField()
    image=models.ImageField()
    
    def __str__(self):
        return self.title