from django.db import models


class FullyUser(models.Model):
    name = models.CharField(max_length=100)
    slackName = models.CharField(max_length=50)
    #email = models.EmailField(max_length=254)


    def __str__(self):
        return self.name

"""
class FullyUserMedals(models.Model):
    fullyUser = models.ForeignKey(FullyUser, on_delete=models.CASCADE)
    medalName = models.CharField(max_length=100)
"""

class FullyBikeTracker(models.Model):
    fullyUser = models.ForeignKey(FullyUser, on_delete = models.CASCADE)
    bikeDate = models.DateField(auto_now=False)