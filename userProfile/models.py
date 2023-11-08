from django.db import models
from userAuth.models import CustomUser as User



class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=50,blank=True)
    website = models.CharField(max_length=100, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True)
    location = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username
