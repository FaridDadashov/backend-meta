from django.db import models
from colorfield.fields import ColorField

# Create your models here.
class Edu_Service(models.Model):
    title=models.CharField(max_length=50)
    image=models.ImageField()
    description=models.TextField()
    about=models.TextField()
    plan=models.TextField()
    color=ColorField(default='#fff')
    
    
    def __str__(self):
      return self.title