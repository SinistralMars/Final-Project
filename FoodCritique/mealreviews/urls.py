from django.urls import path
from .views import indexPageView, searchPageView, restuarantPageView, ratingPageView

urlpatterns = [
    path('', indexPageView, name = 'index'),
    path('Search', searchPageView, name = 'Search'),
    path('Restuarant', restuarantPageView, name = 'Restuarant'),
    path('Rating', ratingPageView, name = 'Rating'),
]