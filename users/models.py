import json

from PIL import Image
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    diet_restrictions = models.CharField(max_length=100000, blank=True)

    def set_profile(self, x):
        self.diet_restrictions = json.dumps(x)

    def get_profile(self):
        return json.loads(self.diet_restrictions)

    def __str__(self):
        return f'{self.user.username} Profile'

