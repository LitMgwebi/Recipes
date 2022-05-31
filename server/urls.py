from django.urls import path
from server import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns=[
     path('recipes', views.index),
     path('createRecipe/', views.create),
     path('recipe/<int:id>', views.recipe),
]

urlpatterns = format_suffix_patterns(urlpatterns)