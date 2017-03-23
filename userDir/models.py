from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.TextField(max_length=100)
    officeLoc = models.TextField(max_length=100)
    slackName = models.TextField(max_length=50)
    hireDate = models.DateField(null=True, blank=True)
    phoneNum = models.TextField(max_length=25)
    jobTitle = models.TextField(max_length=200)
    birthDate = models.DateField(null=True, blank=True)
    photo = models.ImageField(null=True, blank=True)

    def __str__(self):
     return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()