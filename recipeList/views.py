
from django.shortcuts import render_to_response
from dateutil.relativedelta import relativedelta
from django.db.models import Sum
from recipeList.models import *
from datetime import datetime


def shopping_list(request, year, month, day):
    year = int(year)
    month = int(month)
    day = int(day)
    time = datetime(year, month, day)
    items = Meal.objects.all().filter(date__gte=time, date__lt=time + relativedelta(days=6)).values('recipe__ingredient__name', 'recipe__ingredient__unit').annotate(Sum('recipe__ingredient__value'))
    return render_to_response('recipeList/shopping_list.html', {'items': items})
