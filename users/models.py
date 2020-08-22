from django.db import models
from django.contrib.auth.models import User
from django.db.models import ManyToManyField
from multiselectfield import MultiSelectField


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    CHOICES = (
        ('wheat_free', 'Wheat Free'),
        ('vegetarian', 'Vegetarian'),
        ('vegan', 'Vegan'),
        ('nut_free', 'Nut Free'),
        ('soy_free', 'Soy Free'),
        ('organic', 'Organic'),
        ('no_preservatives', 'No Preservatives'),
        ('pork_free', 'Pork Free'),
        ('pescetarian', 'Pescetarian'),
        ('peanut_free', 'Peanut Free'),
        ('sugar_free', 'Sugar Free'),
        ('no_added_sugar', 'No Added Sugar'),
        ('kosher', 'Kosher'),
        ('gluten_free', 'Gluten free'),
        ('fish_free', 'Fish Free'),
        ('egg_free', 'Egg Free'),
        ('diary_free', 'Diary Free'),
        ('non_alcoholic', 'Non Alcoholic'),
    )
    diet_restrictions = MultiSelectField(choices=CHOICES, default=['vegan'])

    def __str__(self):
        return f'{self.user.username} Profile'

