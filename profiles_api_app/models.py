from django.db import models

#use this when overriding django user default model
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

# Create your models here.


class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""
    def create_user(self, email, name, password=None):
        """Create a new user profile"""
        #if email not available
        if not email:
            raise ValueError('Users must have an email address')
        #normalize email - onverting the email to lowercase to maintain consistency.
        email = self.normalize_email(email) 
        #create a new user - user=from baseuermanager model
        user = self.model(email=email, name=name)
        #set password - encrypted
        user.set_password(password)
        #save user
        user.save(using=self._db) 
        return user
    
    def create_superuser(self, email, name, password):
        """Create a new superuser"""
        user = self.create_user(email, name, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user
    

#get all the functionalities and customize
class UserProfile(AbstractBaseUser, PermissionsMixin):
    """db model for user in system"""
    email  = models.EmailField(max_length=255, unique=True) #unique email
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)


    objects = UserProfileManager()


    #overriding default 
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']


    #getting full name
    def get_full_name(self):
        return self.name
    #getting short name
    def get_short_name(self):
        return self.name
    #returning string representation of user
    def __str__(self):
        return self.email
