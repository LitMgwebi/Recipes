from django.urls import path
from .views import index

urlpatterns = [
   path('', index),
   path('list', index),
   path('delete', index),
   path('detail', index),
   path('update', index),
   path('create', index),
]