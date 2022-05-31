from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from .models import Recipes
from .serializers import RecipeSerializer
from rest_framework.decorators import api_view

@api_view(['GET'])
def index(request, format=None):
     recipes = Recipes.objects.all()
     recipeSerializer = RecipeSerializer(recipes, many=True)
     return Response(recipeSerializer.data)
     

@api_view(['POST'])
def create(request, format=None):
     recipeSerializer = RecipeSerializer(data=request.data)
     if recipeSerializer.is_valid():
          recipeSerializer.save()
          return Response(recipeSerializer.data, status=status.HTTP_201_CREATED)


def getOneRecipe(id):
     try:
          recipe = Recipes.objects.get(pk=id)
     except Recipes.DoesNotExist:
          recipe = Response(status=status.HTTP_404_NOT_FOUND)

     return recipe

@api_view(['GET', 'PUT', 'DELETE'])
def recipe(request, id, format=None):
     recipe = getOneRecipe(id)
     
     if request.method == 'GET':
          serializer = RecipeSerializer(recipe)
          return Response(serializer.data)
     elif request.method == 'PUT':
          serializer = RecipeSerializer(recipe, data=request.data)
          if serializer.is_valid():
               serializer.save()
               return Response(serializer.data)
          return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
     elif request.method == 'DELETE':
          recipe.delete()
          return Response(status=status.HTTP_204_NO_CONTENT)
