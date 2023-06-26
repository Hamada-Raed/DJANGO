from django.db import models
import re

class UserManager(models.Manager):
    def regValidator(self, postData):
        errors = {}
        #input validations
        if len(postData['username']) < 2:
            errors['username'] = "First Name should atleast be 2 charecters"
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):    # test whether a field matches the pattern            
            errors['email'] = "Invalid email address!"
        if User.objects.filter(email=postData['email']).exists():
            errors['email'] = "This email is already registered!"
        if len(postData['password'] or postData['password_conf']) < 8:
            errors['password_len'] = "Password should atleast be 8 charecters"
        if postData['password'] != postData['password_conf']:
            errors['password_match'] = "Passwords do not match"
        return errors 

    def loginValidator(self, postData):
        errors = {}  
        if not (User.objects.filter(email=postData['email']) and User.objects.filter(password=postData['password'])):
            errors['login'] = "Login failed! Check email and password"

        return errors 

class User(models.Model):
    username = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class CourseManager(models.Manager): 
    errors = {}
    def course_validator(self, postData):
        if len(postData['name_course']) < 1: 
            errors['name'] = 'Name should be provided'
        if len(postData['name']) < 2: 
            errors['name'] = 'Name should be at least 2 charactor'
        if len(postData['day']) < 1: 
            errors['day'] = "Day should be provided"
        if postData['number'] < 0: 
            errors['number'] = "Number should be a positive"
        if len(postData['desc']) < 1: 
            errors['desc'] = "Description should be porvided"
        
        return errors

class Course(models.Model): 
    name = models.CharField(max_length=255)
    day = models.CharField(max_length=255)
    number = models.BigIntegerField()
    desc = models.TextField()
    Insturctor = models.CharField(max_length=255)
    user = models.ForeignKey(User, related_name="users", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CourseManager()
