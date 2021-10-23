from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django_countries.fields import CountryField


class Profile(models.Model):
    """
    Profile model to maintain
    default delivery and order history
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_phone_number = models.CharField(
        max_length=25, null=True, blank=True)
    default_address1 = models.CharField(
        max_length=100, null=True, blank=True)
    default_address2 = models.CharField(
        max_length=100, null=True, blank=True)
    default_town_or_city = models.CharField(
        max_length=30, null=True, blank=True)
    default_county = models.CharField(
        max_length=20, null=True, blank=True)
    default_postcode = models.CharField(
        max_length=15, null=True, blank=True)
    default_country = CountryField(
        blank_label='Country *', null=True, blank=True)

    def __str__(self):
        return self.user.username


# create profile or update existing
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):

    if created:
        Profile.objects.create(user=instance)
    # Existing users: just save the profile
    instance.profile.save()
