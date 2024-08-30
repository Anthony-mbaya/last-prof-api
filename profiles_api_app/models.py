from django.db import models

#use this when overriding django user default model
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.conf import settings #retrieve settings fom settings.py - AUTH_USER_MODEL

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


class ProfilesFeedItem(models.Model):
    """profile status update"""
    user_profile = models.ForeignKey(
        #specify model you want to set rel with - retrieve form settings .py bcos you man chnge to default user model
        settings.AUTH_USER_MODEL,
        #if user_orifie is deleted the associated feed item shold be deleted as well
        on_delete=models.CASCADE
    )
    blog_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)#automatically add time stamp

    def __str__(self):
        return self.blog_text