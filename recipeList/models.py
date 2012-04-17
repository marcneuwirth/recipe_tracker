from django.db import models


class Recipe(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=200)
    cookingTime = models.IntegerField()

    def __unicode__(self):
        return '%s (%s)' % (self.created_on, self.name)


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
)


class Ingredient(models.Model):
    name = models.CharField(max_length=200)
    value = models.FloatField()
    unit = models.CharField(max_length=32, null=True, blank=True, choices=UNITS)
    instruction = models.CharField(max_length=200, null=True, blank=True)
    recipe = models.ForeignKey(Recipe)

    def __unicode__(self):
        return '%s (%s)' % (self.name, self.value)


class Instruction(models.Model):
    text = models.CharField(max_length=200)
    recipe = models.ForeignKey(Recipe)

    def __unicode__(self):
        return '%s' % (self.text)


class Meal(models.Model):
    date = models.DateField()
    pricePerServing = models.FloatField(null=True, blank=True)
    recipe = models.ForeignKey(Recipe)

    def __unicode__(self):
        return '%s (%s)' % (self.date, self.pricePerServing)

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
        return '%s (%s)' % (self.created_on, self.stars)


class Comment(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=200)
    body = models.TextField()
    meal = models.ForeignKey(Meal)

    def __unicode__(self):
        return '%s (%s)' % (self.name, self.body)
