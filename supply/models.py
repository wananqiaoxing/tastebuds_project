from django.db import models

class Supplier(models.Model):
    supplier_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    position = models.CharField(max_length=128)
    def __str__(self):
        return self.name

class IngredientSupply(models.Model):
    supply_id = models.AutoField(primary_key=True)
    # connect to recipes
    recipe = models.ForeignKey('recipes.Recipe', on_delete=models.CASCADE, related_name='ingredient_supplies')
    #connect to supplier
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name='ingredient_supplies')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    commodity = models.CharField(max_length=128)
#rewrite the supplys to supplies
    class Meta:
        verbose_name_plural = 'Ingredient Supplies'

    def __str__(self):
        return f"Supply {self.supply_id} - {self.commodity}"