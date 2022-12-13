from django.shortcuts import render
from .models import Dish, Restaurant

# Create your views here.
def indexPageView(request) :
    return render(request, "mealreviews/index.html")

def editPageView(request) :
    if request.method == 'POST':
        id = request.POST['id']
        restaurant = Restaurant.objects.get(id=id)
        restaurant.name = request.POST['name']
        restaurant.address = request.POST['address']
        restaurant.score = request.POST['rating']
        restaurant.cuisineType = request.POST['description']

        restaurant.save()

        return render(request, "mealreviews/restaurant.html")


def restaurantPageView(request) :
    data = Restaurant.objects.all()

    context = {
        "restaurants": data
    }
    return render(request, "mealreviews/restaurant.html", context)

def dishPageView(request) :
    if request.method == 'POST' :
        context = {
            'restaurant' : request.POST['restaurant']
        }
        return render(request, "mealreviews/dish.html", context)
    else :
        return render(request, "mealreviews/restaurant.html")

def showPageView(request, id) :
    data = Restaurant.objects.get(id=id)

    context = {
        'restaurant' : data
    }
    return render(request, "mealreviews/show.html", context)

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
    data = Restaurant.objects.get(id=request.POST.get('id'))

    data.delete()

    context = {
        "restaurants": data
    }
    return render(request, "mealreviews/restaurant.html", context)
