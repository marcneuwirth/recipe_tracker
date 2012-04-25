from django.db import models
from django.contrib import admin


class Recipe(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=200)
    cooking_time = models.IntegerField()
    servings = models.IntegerField(null=True, blank=True)
    reference = models.CharField(max_length=200, null=True, blank=True)
    instruction = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return '%s' % (self.name)


UNITS = (
    ('lbs', 'lbs'),
    ('oz', 'oz'),
    ('fl oz', 'fl oz'),
    ('tsp', 'tsp'),
    ('tbs', 'tbs'),
    ('cup', 'cup'),
    ('pint', 'pint'),
    ('quart', 'quart'),
    ('gallon', 'gallon'),
    ('in', 'in'),
    ('slices', 'slices'),
    ('clove', 'clove'),
    ('bunch', 'bunch'),
    ('pinch', 'pinch'),
    ('can', 'can'),
)


class Ingredient(models.Model):
    value = models.FloatField()
    unit = models.CharField(max_length=32, null=True, blank=True, choices=UNITS)
    name = models.CharField(max_length=200)
    instruction = models.CharField(max_length=200, null=True, blank=True)
    recipe = models.ForeignKey(Recipe)

    def __unicode__(self):
        return '%s' % (self.name)

MEALTIMES = (
    ('Breakfast', 'Breakfast'),
    ('Lunch', 'Lunch'),
    ('Dinner', 'Dinner'),
    ('Snack', 'Snack'),
)


class Meal(models.Model):
    date = models.DateField()
    servings = models.IntegerField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    meal_time = models.CharField(max_length=32, null=True, blank=True, choices=MEALTIMES)
    recipes = models.ManyToManyField(Recipe, through='Meal_Recipe')

    class Meta:
        ordering = ['date']

    def __unicode__(self):
        return '%s - %s' % (self.date, self.meal_time)


class Meal_Recipe(models.Model):
    meal = models.ForeignKey(Meal)
    recipe = models.ForeignKey(Recipe)

    class Meta:
        ordering = ['meal__date', 'recipe__name']

    def __unicode__(self):
        return '%s - %s' % (self.meal.date, self.recipe.name)

STARS = (
    ('1', 1),
    ('2', 2),
    ('3', 3),
    ('4', 4),
    ('5', 5),
)


class Rating(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    stars = models.IntegerField(choices=STARS)
    meal_recipe = models.ForeignKey(Meal_Recipe)

    def __unicode__(self):
        return '%s' % (self.stars)


class Comment(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=200)
    body = models.TextField()
    meal_recipe = models.ForeignKey(Meal_Recipe)

    def __unicode__(self):
        return '%s' % (self.name)

