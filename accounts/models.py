from django.db import models
from django.contrib.auth.models import User
class UserProfile(models.Model):
    # connect to the user model
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    gender = models.CharField(max_length=64, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.user.username
