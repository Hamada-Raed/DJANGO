from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=45)
    pages = models.TextField()
    description = models.TextField()
    release_date = models.DateField()
    duration = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
