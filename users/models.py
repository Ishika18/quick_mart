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
        ('wheat-free', 'Wheat Free'),
        ('vegetarian', 'Vegetarian'),
        ('vegan', 'Vegan'),
        ('tree-nut-free', 'Tree Nut Free'),
        ('soy-free', 'Soy Free'),
        ('shellfish-free', 'Shellfish Free'),
        ('sesame-free', 'Sesame Free'),
        ('red-meat-free', 'Red Meat Free'), #kgjkl
        ('pork-free', 'Pork Free'),
        ('pecatarian', 'Pecatarian'),
        ('peanut-free', 'Peanut Free'),
        ('no-oil-added', 'No Oil Added'),
        ('mustard-free', 'Mustard Free'),
        ('lupine-free', 'Lupine Free'),
        ('low-sugar', 'Low Sugar'),
        ('kosher', 'Kosher'),
        ('gluten-free', 'Gluten free'),
        ('fodmap-free', 'Fodmap Free'),
        ('fish-free', 'Fish Free'),
        ('egg-free', 'Egg Free'),
        ('diary-free', 'Diary Free'),
        ('crustacean-free', 'Crustacean Free'),
        ('celery-free', 'Celery Free'),
        ('alcohol-free', 'Alcohol Free'),
    )
    diet_restrictions = MultiSelectField(choices=CHOICES, default=['vegan'])

    def __str__(self):
        return f'{self.user.username} Profile'

