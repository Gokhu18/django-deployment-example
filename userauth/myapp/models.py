from django.db import models

# import basic user model
from django.contrib.auth.models import User


# Create your models here.
class UserProfileInfo(models.Model):

    # user uses default values from basic User model (username,email,password,fname,lname). Directly inheriting from User class may trick db into thinking there are multiple instances of the same user
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    # Add any additional attributes you want
    portfolio = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        # Built-in attribute of django.contrib.auth.models.User !
        return self.user.username
