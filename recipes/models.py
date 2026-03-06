from django.db import models
from django.contrib.auth.models import User

class Recipe(models.Model):
    recipe_id = models.AutoField(primary_key=True)
    # connect to the user
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipes')
    title = models.CharField(max_length=128)
    ingredient = models.TextField()
    content = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # 建议添加（profile.html 用到了）
    image = models.ImageField(upload_to='recipe_images', blank=True, null=True)

    def __str__(self):
        return self.title