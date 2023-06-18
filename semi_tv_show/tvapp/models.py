from django.db import models
from datetime import datetime
from datetime import timedelta

class showManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['title']) < 2:
            errors["title"] = "Title should be at least 2 characters"
        if len(postData['network']) < 2:
            errors["network"] = "Network should be at least 3 characters"
        if len (postData['desc']) > 0:
            if len(postData['desc']) < 10:
                errors["desc"] = " Description should be at least 10 characters"
        if  postData['release_date'] < str(datetime.now()):
            errors['release_date'] = "Your input date is in the past" 
        return errors

class show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=200)
    release_date = models.DateField()
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = showManager()
