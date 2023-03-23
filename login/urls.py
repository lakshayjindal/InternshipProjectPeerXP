from django.urls import path
from .views import *



urlpatterns = [
    path('', index, name='Login'),
    path('logout', logout_func, name='logout'),
    path('search', search, name='search')
]
