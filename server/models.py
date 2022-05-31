from django.db import models

# Create your models here.
class Recipes(models.Model):
     RecipeId = models.AutoField(primary_key=True)
     Serving = models.IntegerField()
     Description = models.TextField()
     Method = models.TextField()
     Picture = models.ImageField(upload_to="files/covers")