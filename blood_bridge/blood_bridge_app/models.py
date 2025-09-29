from django.db import models

class Donor(models.Model):
    name = models.CharField(max_length=100)
    blood_type = models.CharField(max_length=3)
    last_donation = models.DateField(null=True, blank=True)