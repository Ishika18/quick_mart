from django.db import models
from django.contrib.auth.models import User
from django.db.models import ManyToManyField
from multiselectfield import MultiSelectField


# class DietRestrictions(models.Model):
#     CHOICES = (
#         ('vegan', 'vegan'),
#         ('vegetarian', 'vegetarian'),
#         ('gluten-free', 'gluten-free'),
#         ('wheat-free', 'wheat-free'),
#         ('tree-nut-free', 'tree-nut-free'),
#         ('soy-free', 'soy-free'),
#         ('shellfish-free', 'shellfish-free'),
#         ('sesame-free', 'sesame-free'),
#         ('low-sugar', 'low-sugar'),
#         ('no-oil-added', 'no-oil-added'),
#         ('mustard-free', 'mustard-free')
#     )
#     diet_restrictions = MultiSelectField(choices=CHOICES)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.CharField(default='test', max_length=100)
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
    diet_restrictions = MultiSelectField(choices=CHOICES, default=['vegan'])

    def __str__(self):
        return f'{self.user.username} Profile'

