from django.shortcuts import render
from django.http import HttpResponse
from .models import Cup


# Create your views here.
def index(request):
    return HttpResponse("Test URL")


def name(request, name):
    return HttpResponse("Hello " + name)

def times2(request, answer):
    return HttpResponse("The product times 2 is: " + str(2 * answer))

# name, material, and manufacturerDate

# function that adds each number to the number written in the url
def total(request, numbers):
    sum = 0
    for nums in range(0, numbers+1):
        sum += nums
    return HttpResponse(sum)


# function that makes a new cup using a constructor
def new(request):
    newCup = Cup(name="canteen", material="plastic", manufacturerDate="2018-09-04")
    newCup.save()
    return HttpResponse("New Cup added!!!")

# function made wihtout a cun
def new2(request):
    allCups = Cup.objects.all()
    newCup2 = Cup.objects.create(name="waterbottle", material="plastic", manufacturerDate="2019-01-03")
    return HttpResponse(allCups)




