from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def indexPageView(request) :
    return render(request, "mealreviews/index.html")
def searchPageView(request) :
    return render(request, "mealreviews/search.html")
def restaurantPageView(request) :
    return render(request, "mealreviews/restaurant.html")
def ratingPageView(request) :
    return render(request, "mealreviews/rating.html")
def createPageView(request) :
    return render(request, "mealreviews/create.html")
def deletePageView(request) :
    return render(request, "mealreviews/delete.html")
