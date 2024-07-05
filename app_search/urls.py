from django.urls import path

from .views import all_search

urlpatterns = [
    path('search/', all_search, name='search')
]
