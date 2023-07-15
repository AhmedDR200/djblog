from django.db import models

# Create your models here.

CATEGORY_CHOICES = (
    ('WB', 'web development'),
    ('DB', 'desktop development'),
    ('PB', 'python development'),
)

class Post(models.Model):
    title = models.CharField(max_length=50 , unique=True)
    contant = models.TextField(max_length=5000)
    created_at = models.DateTimeField()
    published = models.BooleanField(default=True)
    email = models.EmailField(max_length=254 , null=True , blank=True)
    views_count = models.PositiveIntegerField(default=0)
    category = models.CharField (choices=CATEGORY_CHOICES , max_length=20)



    def __str__(self):
      return self.title
