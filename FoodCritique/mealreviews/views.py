from django.shortcuts import render
from django.http import HttpResponse
from .models import Dish, Restaurant

# Create your views here.
def indexPageView(request) :
    return render(request, "mealreviews/index.html")
def searchPageView(request) :
    return render(request, "mealreviews/search.html")
def restaurantPageView(request) :
    data = Restaurant.objects.all()

    context = {
        "restaurants": data
    }
    return render(request, "mealreviews/restaurant.html")
def ratingPageView(request) :
    return render(request, "mealreviews/rating.html")

def createPageView(request) :
    if request.method == 'POST':
        new_dish = Dish()
        new_dish.restaurant = Restaurant.objects.get(id=request.POST.get('restaurant'))
        new_dish.name = request.POST['name']
        new_dish.score = request.POST['rating']
        new_dish.description = request.POST['description']
        new_dish.save()

        return render(request, "mealreviews/index.html")

    else:
        data = Restaurant.objects.all()
        context = {
            "restaurants": data
        }
        return render(request, "mealreviews/create.html", context)

def deletePageView(request) :
    return render(request, "mealreviews/delete.html")
