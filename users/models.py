from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField


class DietRestrictions(models.Model):
    CHOICES = (
        ('vegan', 'vegan'),
        ('vegetarian', 'vegetarian'),
        ('gluten-free', 'gluten-free'),
        ('wheat-free', 'wheat-free'),
        ('tree-nut-free', 'tree-nut-free'),
        ('soy-free', 'soy-free'),
        ('shellfish-free', 'shellfish-free'),
        ('sesame-free', 'sesame-free'),
        ('low-sugar', 'low-sugar'),
        ('no-oil-added', 'no-oil-added'),
        ('mustard-free', 'mustard-free')
    )
    diet_restrictions = MultiSelectField(choices=CHOICES, blank=True)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    diet_restrictions = models.ManyToManyField(DietRestrictions)

    def __str__(self):
        return f'{self.user.username} Profile'

