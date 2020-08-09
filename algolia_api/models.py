from django.db import models

# Create your models here.


class DietRestrictions(models.Model):
    label = models.CharField(max_length=100)
    show_name = models.CharField(max_length=100)
    object_id = models.CharField(max_length=100)
