from django.db import models
from django.contrib import admin


class Recipe(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=200)
    cookingTime = models.IntegerField()
    reference = models.URLField(null=True, blank=True)
    instruction = models.TextField(null=True, blank=True)

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


class Meal(models.Model):
    date = models.DateField()
    pricePerServing = models.FloatField(null=True, blank=True)
    recipe = models.ForeignKey(Recipe)

    def __unicode__(self):
        return '%s' % (self.date)

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
    meal = models.ForeignKey(Meal)

    def __unicode__(self):
        return '%s' % (self.stars)


class Comment(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=200)
    body = models.TextField()
    meal = models.ForeignKey(Meal)

    def __unicode__(self):
        return '%s' % (self.name)

