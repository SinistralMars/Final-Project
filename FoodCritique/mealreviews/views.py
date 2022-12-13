from django.shortcuts import render

# Create your views here.
def indexPageView(request) :
    return render(request, "mealreviews/index.html")
def searchPageView(request) :
    return render(request, "mealreviews/search.html")
def restaurantPageView(request) :
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
    return render(request, "mealreviews/create.html")
def deletePageView(request) :
    return render(request, "mealreviews/delete.html")
