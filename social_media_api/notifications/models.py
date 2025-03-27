from django.db import models
from django.contrib.auth.models import User 
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.conf import settings

# Create your models here.
class Notification(models.Model):
    recipient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="notifications_received")
    actor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="notifications_sent")
    verb = models.CharField(max_length=255)
    target = models.CharField(max_length=255, blank=True, null=True)
    is_read = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.actor} {self.verb} {self.target} ({'Read' if self.is_read else 'unread'})"
    