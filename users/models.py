from django.db import models
from django.contrib.auth.models import User
from django.db.models import ManyToManyField
from multiselectfield import MultiSelectField


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.CharField(default='test', max_length=100)
    CHOICES = (
        ('wheat_free', 'Wheat Free'),
        ('vegetarian', 'Vegetarian'),
        ('vegan', 'Vegan'),
        ('tree_nut_free', 'Tree Nut Free'),
        ('soy_free', 'Soy Free'),
        ('shellfish_free', 'Shellfish Free'),
        ('sesame_free', 'Sesame Free'),
        ('red_meat_free', 'Red Meat Free'),
        ('pork_free', 'Pork Free'),
        ('pecatarian', 'Pecatarian'),
        ('peanut_free', 'Peanut Free'),
        ('no_oil_added', 'No Oil Added'),
        ('mustard_free', 'Mustard Free'),
        ('lupine_free', 'Lupine Free'),
        ('low_sugar', 'Low Sugar'),
        ('kosher', 'Kosher'),
        ('gluten_free', 'Gluten free'),
        ('fodmap_free', 'Fodmap Free'),
        ('fish_free', 'Fish Free'),
        ('egg_free', 'Egg Free'),
        ('diary_free', 'Diary Free'),
        ('crustacean_free', 'Crustacean Free'),
        ('celery_free', 'Celery Free'),
        ('alcohol_free', 'Alcohol Free'),
    )
    diet_restrictions = MultiSelectField(choices=CHOICES, default=['vegan'])

    def __str__(self):
        return f'{self.user.username} Profile'

