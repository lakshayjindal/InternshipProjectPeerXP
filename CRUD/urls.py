from django.urls import path
from .views import *

urlpatterns = [
    path('delete', delete),
    path('update', update),
    path('create', create),
]
