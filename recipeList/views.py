from django.shortcuts import render_to_response
from django.template import RequestContext
from dateutil.relativedelta import relativedelta
from django.db.models import Sum, Avg, Count, F, Q
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

    items = Meal.objects \
        .filter(date__gte=dateFrom, date__lt=dateTo) \
        .filter(Q(meal_recipe__recipe__ingredient__ingredient_type__isnull=True) | Q(meal_recipe__recipe__ingredient__ingredient_type=F('meal_recipe__meal_type'))) \
        .values('meal_recipe__recipe__ingredient__name', 'meal_recipe__recipe__ingredient__unit', 'meal_recipe__recipe__servings', 'meal_recipe__servings') \
        .annotate(Sum('meal_recipe__recipe__ingredient__value')) \
        .order_by()

    print items.query
    return render_to_response('recipeList/shopping_list.html', {'items': items, 'dateFrom': dateFrom, 'dateTo': dateTo}, RequestContext(request))


def ingredient_detail(request, name):
    recipe_list = Recipe.objects.filter(ingredient__name=name)
    return render_to_response('recipeList/recipe_list.html', {'recipe_list': recipe_list, 'ingredient': name}, RequestContext(request))


def all_ingredients(request):
    ingredients = Ingredient.objects.all().values('name').annotate(Count("id")).order_by()
    return render_to_response('recipeList/ingredients_list.json', {'ingredients': ingredients}, mimetype="application/json")


def meal_detail(request, pk):
    meals = Meal.objects.filter(pk=pk)
    return render_to_response('recipeList/meal_list.html', {'meal_list': meals}, RequestContext(request))


def meal_recipe_detail(request, pk):
    meals = Meal_Recipe.objects.filter(pk=pk)
    if request.method == 'POST':
        if 'star' in request.POST and str(request.POST['star']) is not '':
            meals[0].rating_set.create(stars=request.POST['star'])
        if 'name' in request.POST and str(request.POST['name']) is not '' and 'body' in request.POST and str(request.POST['body']) is not '':
            print request.POST
            meals[0].comment_set.create(name=request.POST['name'], body=request.POST['body'])

    # meals = meals.annotate(avg_rating=Avg('rating__stars'))

    return render_to_response('recipeList/meal_recipe_detail.html', {'meal': meals[0]}, RequestContext(request))


def today(request):
    today = date.today()
    tomorrow = today + relativedelta(days=1)
    meal_list = Meal.objects.filter(date__gte=today, date__lt=tomorrow)
    return render_to_response('recipeList/meal_list.html', {'meal_list': meal_list, 'today': today}, RequestContext(request))
