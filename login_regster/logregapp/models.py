from django.db import models

class UserManager(models.Manager): 
    def reg_validator(self, postData): 
        errors={}
        if len(postData['fname']) < 2 or not postData['fname'].isalpha(): 
            errors['fname'] = "First name should be at least 2 chars and contains letters only"
        if len(postData['lname']) < 2 or not postData['lname'].isalpha(): 
            errors['lname'] = "Last name should be at least 2 chars and contains letters only"
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):             
            errors['email'] = "Invalid email address!"
        if  len(postData['password']) < 8 :    
            errors['password'] = "The password must be 8 characters minimum"
        if postData['password'] != postData['password_confirm']:
            errors['password'] = "Passwords are note the same"
        return errors 

    def log_validator(self, postData): 
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        errors2 = {}
        email_log = postData['email_log']
        password_log = postData['password_log'] 
        user = User.objects.filter(email=email_log) 
        if len(email_log) < 2: 
            errors2('email_log') == "Email cannot be empty!" 
        elif not EMAIL_REGEX.match(email_log):
            errors2["email_log"] = "Invalid Email Address!"
        elif not bcrypt.checkpw(password2.encode(), user[0].password.encode()):
            errors2["password_log"] = "Incorrect password. Try again!"
        
        return errors2

class User(models.Model): 
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager() 
