from django.urls import path
from .views import indexPageView, searchPageView, restaurantPageView, ratingPageView, createPageView, deletePageView, dishPageView

urlpatterns = [
    path('create', createPageView, name = 'create'), #Create
    path('search', searchPageView, name = 'search'), #Read
    path('dish', dishPageView, name = 'dish'), #Read
    path('restaurant', restaurantPageView, name = 'restaurant'), #Update
    path('delete', deletePageView, name = 'delete'), #Delete
    path('', indexPageView, name = 'index'),
]