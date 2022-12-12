from django.urls import path
from .views import indexPageView, searchPageView, restaurantPageView, ratingPageView, createPageView, deletePageView

urlpatterns = [
    path('create', createPageView, name = 'create'), #Create
    path('search', searchPageView, name = 'search'), #Read
    path('rating', ratingPageView, name = 'rating'), #Read
    path('restaurant', restaurantPageView, name = 'restaurant'), #Update
    path('delete', deletePageView, name = 'delete'), #Delete
    path('', indexPageView, name = 'index'),
]