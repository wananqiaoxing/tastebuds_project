from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.urls import reverse
class UserProfile(models.Model):
    # connect to the user model
    user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)

    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    gender = models.CharField(max_length=64, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        #new profile for new user register
        profile = UserProfile.objects.create(user=instance)

        #create user URL
        path = reverse('accounts:profile', kwargs={'username': instance.username})
        profile.website = f"http://127.0.0.1:8000{path}"
        profile.save()
