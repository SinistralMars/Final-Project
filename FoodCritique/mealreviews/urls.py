from django.urls import path
from .views import indexPageView, searchPageView, restuarantPageView, ratingPageView, createPageView, deletePageView

urlpatterns = [
    path('', indexPageView, name = 'index'),
    
    path('Create', createPageView, name = 'Create'), #Create
    path('Search', searchPageView, name = 'Search'), #Read
    path('Rating', ratingPageView, name = 'Rating'), #Read
    path('Restuarant', restuarantPageView, name = 'Restuarant'), #Update
    path('Delete', deletePageView, name = 'Delete'), #Delete
]