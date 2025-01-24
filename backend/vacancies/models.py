import uuid
from datetime import datetime, timedelta, timezone

from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=32)
    
      
    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name_plural = 'Categories'


EXPERIENCE_CHOICES = (
    ('Təcrubəli Kadr', 'experienced'),
    ('Təcrübə tələb olunmur', 'entry'),
)

class Vacancy(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=32)
    description = models.TextField()
    experience = models.CharField(max_length=40, choices=EXPERIENCE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    @property
    def is_new(self):
        return (datetime.now(timezone.utc) - self.created_at) < timedelta(days=3)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Vacancies'
    