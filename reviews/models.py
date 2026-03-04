from django.db import models
from django.contrib.auth.models import User

class Review(models.Model):
    review_id = models.AutoField(primary_key=True)
    #connect to user
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    # connect to restaurant
    restaurant = models.ForeignKey('restaurants.Restaurant', on_delete=models.CASCADE, related_name='reviews')
    # connect to recipes
    recipe = models.ForeignKey('recipes.Recipe', on_delete=models.CASCADE, related_name='reviews')
    content = models.TextField()

    def __str__(self):
        return f"Review {self.review_id} by {self.user.username}"