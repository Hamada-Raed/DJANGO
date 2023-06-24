from django.db import models
import re
import bcrypt   

class UserManager(models.Manager): 
    def Register_validator(self, postData):
        errors = {}
        if len(postData['fname']) < 2 or not postData['fname'].isalpha() :
            errors['fname'] = 'The first name should be at least 2 charactor' 
        if len(postData['lname']) < 2 or not postData['lname'].isalpha() :
            errors['lname'] = 'The last name should be at least 2 charactor' 
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):    # test whether a field matches the pattern            
            errors['email'] = "Invalid email address!"
        if len(postData['password']) < 8: 
            errors['password'] = 'The Password should be at least 8 charactor'
        if postData['password'] != postData['password_confirm']:
            errors['password'] = "Passwords are note the same"
        
        return errors

    def Login_validator(self, postData): 
        errors2 = {}
        

class User(models.Model): 
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()