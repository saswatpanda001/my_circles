from django.dispatch import receiver
from django.db.models.signals import post_save
from profiles.models import Profile_Model
from django.contrib.auth import get_user_model
User = get_user_model()
from django.dispatch import receiver


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    print(sender, instance, created)
    if created:
        Profile_Model.objects.create(user=instance)
