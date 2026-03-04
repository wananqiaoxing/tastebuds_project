from django.db import models


class Restaurant(models.Model):
    restaurant_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    position = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Menu(models.Model):
    menu_id = models.AutoField(primary_key=True)
    # connect to restaurants
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='menus')
    # connect to recipes
    recipe = models.ForeignKey('recipes.Recipe', on_delete=models.CASCADE, related_name='menus')

    def __str__(self):
        return f"Menu {self.menu_id} - {self.restaurant.name}"

