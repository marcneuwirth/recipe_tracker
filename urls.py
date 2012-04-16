from django.conf.urls.defaults import patterns, include, url
from django.views.generic import ListView, DetailView
from recipeList.models import *

# Default Views
recipe_detail = DetailView.as_view(model=Recipe)
recipe_list = ListView.as_view(model=Recipe)
# meal_detail = DetailView.as_view(model=Meal)
meal_list = ListView.as_view(model=Meal)

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


class IngredientInline(admin.TabularInline):
    model = Ingredient


class InstructionInline(admin.TabularInline):
    model = Instruction


class RecipeAdmin(admin.ModelAdmin):
    inlines = [IngredientInline, InstructionInline]

admin.site.register(Recipe, RecipeAdmin)

admin.site.register(Meal)
admin.site.register(Rating)
admin.site.register(Comment)

urlpatterns = patterns('',
    url(r'^recipe/(?P<pk>[a-z\d]+)/$', recipe_detail, name='recipe_detail'),
    url(r'^$', recipe_list, name='recipe_list'),

    url(r'^meal/(?P<pk>[a-z\d]+)/$', 'recipeList.views.meal_detail', name='meal_detail'),
    url(r'^meals/$', meal_list, name='meal_list'),

    url(r'^shoppinglist/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d\d?)$', 'recipeList.views.shopping_list', name='shoppinglist'),
    url(r'^shoppinglist/$', 'recipeList.views.shopping_list', name='shoppinglistNow'),

    url(r'^ingredient/(?P<pk>[a-z\d]+)/$', 'recipeList.views.ingredient_detail', name='ingredient_detail'),

    url(r'^today/$', 'recipeList.views.today', name='today'),
    # Examples:
    # url(r'^$', 'recipes.views.home', name='home'),
    # url(r'^recipes/', include('recipes.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
