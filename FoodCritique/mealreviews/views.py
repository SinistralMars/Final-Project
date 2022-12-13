from django.shortcuts import render, redirect
from django.db.models import Avg
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
        restaurant.cuisineType = request.POST['description']

        restaurant.save()

        return redirect('restaurant')


def restaurantPageView(request) :
    data = Restaurant.objects.all().annotate(average_value=Avg('dish__score'))

    context = {
        "restaurants": data,
    }
    return render(request, "mealreviews/restaurant.html", context)

def dishPageView(request) :
    id = request.GET['id']
    data = Dish.objects.all().filter(restaurant_id=id)

    restaurant = Restaurant.objects.get(id=id)

    context = {
        'dishes' : data,
        'restaurant' : restaurant
    }
    return render(request, "mealreviews/dish.html", context)

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

def addRestaurantPageView(request) :
    if request.method == 'POST' :
        new_restaurant = Restaurant()
        new_restaurant.name = request.POST['name']
        new_restaurant.address = request.POST['address'] 
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
    data = Restaurant.objects.get(id=request.POST.get('id'))

    data.delete()

    context = {
        "restaurants": data
    }
    return redirect('restaurant')

def deleteDishPageView(request) :
    data = Dish.objects.get(id=request.POST.get('id'))

    data.delete()

    context = {
        "dishes": data
    }
    return redirect('restaurant')