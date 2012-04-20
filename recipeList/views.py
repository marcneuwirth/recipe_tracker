from django.shortcuts import render_to_response
from django.template import RequestContext
from dateutil.relativedelta import relativedelta
from django.db.models import Sum, Avg, Count
from recipeList.models import *
from datetime import datetime, date


def shopping_list(request, year=None, month=None, day=None):
    try:
        year = int(year)
        month = int(month)
        day = int(day)
        dateFrom = date(year, month, day)
    except:
        dateFrom = date.today()

    dateTo = dateFrom + relativedelta(days=6)

    items = Meal.objects.filter(date__gte=dateFrom, date__lt=dateTo).values('recipe__ingredient__name', 'recipe__ingredient__unit').annotate(Sum('recipe__ingredient__value'))
    return render_to_response('recipeList/shopping_list.html', {'items': items, 'dateFrom': dateFrom, 'dateTo': dateTo}, RequestContext(request))


def ingredient_detail(request, pk):
    ingredient = Ingredient.objects.get(pk=pk)
    recipe_list = Recipe.objects.filter(ingredient__pk=pk)
    return render_to_response('recipeList/recipe_list.html', {'recipe_list': recipe_list, 'ingredient': ingredient}, RequestContext(request))


def all_ingredients(request):
    ingredients = Ingredient.objects.all().values('name').annotate(Count("id")).order_by()
    return render_to_response('recipeList/ingredients_list.json', {'ingredients': ingredients}, mimetype="application/json")


def meal_detail(request, pk):
    meals = Meal.objects.filter(pk=pk)
    if request.method == 'POST':
        if 'star' in request.POST:
            meals[0].rating_set.create(stars=request.POST['star'])
        if 'name' in request.POST and 'body' in request.POST:
            meals[0].comment_set.create(name=request.POST['name'], body=request.POST['body'])

    meals = meals.annotate(avg_rating=Avg('rating__stars'))

    return render_to_response('recipeList/meal_detail.html', {'meal': meals[0]}, RequestContext(request))


def today(request):
    today = date.today()
    tomorrow = today + relativedelta(days=1)
    meal_list = Meal.objects.filter(date__gte=today, date__lt=tomorrow)
    return render_to_response('recipeList/meal_list.html', {'meal_list': meal_list, 'today': today}, RequestContext(request))
