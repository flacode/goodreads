from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator

class Book(models.Model):
    CATEGORIES = (
        ('fiction', 'fiction'),
        ('fantasy', 'fantasy'),
        ('art', 'art')
    )
    title = models.CharField(max_length=128)
    author = models.CharField(max_length=128)
    summary = models.TextField()
    no_pages = models.IntegerField(validators=[MinValueValidator(0)], blank=True, null=True)
    current_page = models.IntegerField(blank=True, null=True)
    complete = models.BooleanField(default=False)
    category = models.CharField(max_length=20, choices=CATEGORIES)

    def __str__(self):
       return self.title
