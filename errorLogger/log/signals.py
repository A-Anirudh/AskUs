from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Log, Notification


@receiver(post_save, sender=Log)
def create_notif(sender, instance, created, **kwargs):

    if created:
        Notification.objects.create(user=instance.author, notification_for='log created', title=instance)


