from django.db import models

class showManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['title']) < 2:
            errors["title"] = "Title should be at least 2 characters"
        if len(postData['network']) < 2:
            errors["network"] = "Network should be at least 3 characters"
        if len(postData['desc']) < 10:
            errors["desc"] = " description should be at least 10 characters"
        return errors

class show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=200)
    release_date = models.DateField()
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = showManager()
