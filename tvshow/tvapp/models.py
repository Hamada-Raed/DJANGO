from django.db import models

class show(models.Model):
    name = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    desc = models.TextField()
    release_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
