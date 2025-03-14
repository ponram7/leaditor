from django.db import models

class Lead(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    industry = models.CharField(max_length=100, blank=True, null=True)
    website_visits = models.PositiveIntegerField(default=0)
    email_open_rate = models.FloatField(default=0.0)
    score = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name
