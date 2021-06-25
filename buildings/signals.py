from django.db.models.signals import post_save
from django.dispatch import receiver

from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.models import Group


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        print('Profile created!')


# post_save.connect(create_profile, sender=User)

@receiver(post_save, sender=User)
def update_user(sender, instance, created, **kwargs):
    if not created:
        instance.profile.save()
        #print(instance.groups)
        print('User updated!')

# post_save.connect(update_user, sender=User)


# remove the old group giati prepei na einai h to ena h to allo
@receiver(post_save, sender=Profile)
def update_profile(sender, instance, created, **kwargs):
    role = instance.role
    if role == 'TENANT':
        group = Group.objects.get(name='Tenants')
        instance.user.groups.add(group)
    elif role == 'ADMINISTRATOR':
        group = Group.objects.get(name='Administrators')
        instance.user.groups.add(group)
    elif role == 'SITE_ADMIN':
        group = Group.objects.get(name='Site-admin')
        instance.user.groups.add(group)

    print('Profile Updated')

