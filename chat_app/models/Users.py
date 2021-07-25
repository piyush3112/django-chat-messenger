from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.contrib.auth.signals import user_logged_in, user_logged_out


class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    status = models.BooleanField(default=False)


def set_status(sender, **kwagrs):
    if kwagrs['created']:
        user_profile = UserProfile.objects.create(user=kwagrs['instance'])

def update_status_login(sender, user, request, **kwargs):
      UserProfile.objects.filter(user=user).update(status=True)

def update_status_logout(sender, user, request, **kwargs):
      UserProfile.objects.filter(user=user).update(status=False)

post_save.connect(set_status, sender=User)
user_logged_in.connect(update_status_login, sender=User)
user_logged_out.connect(update_status_logout, sender=User)


