from django.db import models


class Recipe(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=200)
    cookingTime = models.IntegerField()

    def __unicode__(self):
        return '%s (%s)' % (self.created_on, self.name)


class Ingredient(models.Model):
    name = models.CharField(max_length=200)
    value = models.FloatField()
    unit = models.CharField(max_length=32, null=True, blank=True)
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
    date = models.DateTimeField()
    pricePerServing = models.FloatField()
    recipe = models.ForeignKey(Recipe)

    def __unicode__(self):
        return '%s (%s)' % (self.date, self.pricePerServing)


class Rating(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    stars = models.IntegerField()
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
