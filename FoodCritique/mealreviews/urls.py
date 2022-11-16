from django.urls import path
from .views import indexPageView, searchPageView, restuarantPageView, ratingPageView, createPageView, deletePageView

urlpatterns = [
    path('', indexPageView, name = 'index'),
    
    path('create', createPageView, name = 'create'), #Create
    path('search', searchPageView, name = 'search'), #Read
    path('rating', ratingPageView, name = 'rating'), #Read
    path('restuarant', restuarantPageView, name = 'restuarant'), #Update
    path('delete', deletePageView, name = 'delete'), #Delete
]