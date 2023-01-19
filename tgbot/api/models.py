from django.db import models


class BotUser(models.Model):
    registration = models.DateField()
    channel = models.CharField(max_length=255)
    user_id = models.IntegerField(unique=True)
    username = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    email = models.CharField(max_length=255, blank=True)  # models.EmailField()
    mobile = models.CharField(max_length=255, blank=True)
    link = models.CharField(max_length=255, blank=True)
    utm_source = models.CharField(max_length=255, blank=True)
    utm_campaign = models.CharField(max_length=255, blank=True)
    utm_medium = models.CharField(max_length=255)
    utm_term = models.CharField(max_length=255, blank=True)
    utm_content = models.CharField(max_length=255, blank=True)
    last_visit = models.DateField()

    def __str__(self):
        return self.username
