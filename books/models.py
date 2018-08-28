from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator

class Book(models.Model):
    CATEGORIES = (
        ('fiction', 'Fiction'),
        ('fantasy', 'Fantasy'),
        ('art', 'Art')
    )
    title = models.CharField(max_length=128)
    author = models.CharField(max_length=128)
    summary = models.TextField()
    no_pages = models.IntegerField('Number of pages', validators=[MinValueValidator(0)])
    current_page = models.IntegerField(blank=True, null=True)
    complete = models.BooleanField(default=False)
    category = models.CharField(max_length=20, choices=CATEGORIES)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
       return self.title
