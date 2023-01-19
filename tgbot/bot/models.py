from django.db import models


# Create your models here.
class DBRec(models.Model):
    registration = models.DateField(),
    channel = models.CharField(),
    id = models.IntegerField(),
    username = models.CharField(max_length=255),
    first_name = models.CharField(max_length=255),
    last_name = models.CharField(max_length=255),
    email = models.EmailField(),
    mobile = models.CharField(max_length=255),
    link = models.CharField(max_length=255),
    utm_source = models.CharField(max_length=255),
    utm_campaign = models.CharField(max_length=255),
    utm_medium = models.CharField(max_length=255),
    utm_term = models.CharField(max_length=255),
    utm_content = models.CharField(max_length=255),
    last_visit = models.DateField()

    def __str__(self):
        return self.username

