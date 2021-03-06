
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render_to_response
import datetime
from yam.models import Recipe, RecipeIngredient, ContainedIngredient


def hello(request):
    return HttpResponse("<html><head></head><body><strong>hello</strong> world<body>")

def recipeIngredients (request, recipeID):
    thisRecipe = Recipe.objects.get (id=recipeID)
    ingredients = thisRecipe.recipeingredient_set.all ()
    return render_to_response ( "recipe_ingredients.html", {"recipeIngredient_set": ingredients} )

def addIngredient (request, recipeID):
    containedIngredients = ContainedIngredient.objects.all ()
    return render_to_response ( "add_ingredient.html", {"recipeID": recipeID, "containedIngredients": containedIngredients} )

def saveNewIngredient (request):
    recipeID = request.POST ["recipeID"]
    quantity = request.POST ["quantity"]
    containedIngredientID = request.POST ["containedIngredientID"]

    recipe   = Recipe.objects.get ( id = recipeID )
    containedIngredient = ContainedIngredient.objects.get ( id = containedIngredientID)
    ingredient = RecipeIngredient ()
    ingredient.save ()
    ingredient.recipe = recipe
    ingredient.containedIngredient = containedIngredient
    ingredient.quantity = quantity
    ingredient.save ()

    return HttpResponseRedirect('/recipe_ingredients/' + recipeID + "/" )

def time(request):
    now = datetime.datetime.now()
    return render_to_response ( "mypage.html", { "current_date": now } )

def hoursAhead (request, offset):
    try: 
        offset = int (offset)
    except ValueError:
        raise Http404 ()
    dt = datetime.datetime.now () + datetime.timedelta (hours = offset )
    html = "<html><body>In %s, it will be %s" %( offset, dt )
    return HttpResponse (html)

