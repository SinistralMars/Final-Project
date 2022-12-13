from django.urls import path
from .views import indexPageView, editPageView, restaurantPageView, showPageView, createPageView, deletePageView, dishPageView, addRestaurantPageView

urlpatterns = [
    path('create', createPageView, name = 'create'), #Create
    path('edit', editPageView, name = 'edit'), #Read
    path('dish', dishPageView, name = 'dish'), #Read
    path('restaurant', restaurantPageView, name = 'restaurant'), #Update
    path('delete', deletePageView, name = 'delete'), #Delete
    path('addRestaurant', addRestaurantPageView, name = 'addRestaurant'),
    path('', indexPageView, name = 'index'),
    path('show/<int:id>', showPageView, name='show')
]