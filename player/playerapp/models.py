from django.db import models

class playerManager(models.Manager):
    def basic_vaildater(self, post_date): 
        errors = {}
    
        if len (post_date['first_name']) < 2: 
            errors['first_name'] = "First name  must be at least 2 cha--"
        
        if len (post_date['last_name']) < 2: 
            errors['last_name'] = "Last name  must be at least 2 cha--"
        
        if len (post_date['team']) < 2: 
            errors['team'] = "Team must be at least 2 cha--" 
        return errors 

class Player(models.Model):
    first_name = models.CharField(max_length = 255)   
    last_name = models.CharField(max_length = 255)   
    team = models.CharField(max_length = 255)  
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = playerManager()

    
  