from django.db import models

class CourseManager(models.Manager): 
    def basic_validator(self, postData):
        errors={}
        if len(postData['name']) < 5: 
            errors['name'] = "Course name should at least 5 character " 
        if len(postData['desc']) < 15: 
            errors['desc'] = "Description should at least 15 character " 
        
        return errors

class Course(models.Model): 
    name = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CourseManager()
