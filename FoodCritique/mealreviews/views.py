from django.shortcuts import render
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

def dishPageView(request) :
    if request.method == 'POST' :
        context = {
            'restaurant' : request.POST['restaurant']
        }
        return render(request, "mealreviews/dish.html", context)
    else :
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

def addRestaurantPageView(request) :
    if request.method == 'POST' :
        new_restaurant = Restaurant()
        new_restaurant.name = request.POST['name']
        new_restaurant.address = request.POST['address'] 
        new_restaurant.score = request.POST['score']
        new_restaurant.cuisineType = request.POST['cuisineType']

        new_restaurant.save()
        
        data = Restaurant.objects.all()
        context = {
            "restaurants": data
        }
        return render(request, "mealreviews/create.html", context)

    else :
        return render(request, 'mealreviews/addRestaurant.html')

def deletePageView(request) :
    return render(request, "mealreviews/delete.html")
