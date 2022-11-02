from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def indexPageView(request) :
    return HttpResponse("index")
def searchPageView(request) :
    return HttpResponse("Search")
def restuarantPageView(request) :
    return HttpResponse("Restuarant")
def ratingPageView(request) :
    return HttpResponse("Rating")
def createPageView(request) :
    return HttpResponse("Create")
def deletePageView(request) :
    return HttpResponse("Delete")