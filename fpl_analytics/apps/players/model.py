from django.db import models
from django.contrib.auth.models import User

class Player(models.Model):
    name = models.CharField(max_length=100)
    team = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'players'

    def __unicode__(self):
        return u"%s's Subscription Info" % self.user_rec