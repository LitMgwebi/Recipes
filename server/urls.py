from django.urls import path
from server import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns=[
     path('recipes', views.index),
     path('add/', views.create),
     path('detail/<int:id>', views.detail),
     path('edit/<int:id>', views.edit),
     path('delete/<int:id>', views.delete),
]

urlpatterns = format_suffix_patterns(urlpatterns)