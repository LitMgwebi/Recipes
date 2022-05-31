from django.contrib import admin
from .models import Recipes

# Register your models here.

class RecipeAdmin(admin.ModelAdmin):
     readonly_fields = ('RecipeId',)
     
admin.site.register(Recipes, RecipeAdmin)