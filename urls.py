from django.conf.urls.defaults import patterns, include, url
from django.views.generic import ListView, DetailView
from recipeList.models import *

# Default Views
recipe_detail = DetailView.as_view(model=Recipe)
recipe_list = ListView.as_view(model=Recipe)

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

urlpatterns = patterns('',
    url(r'^recipe/(?P<pk>[a-z\d]+)/$', recipe_detail, name='recipe_detail'),
    url(r'^$', recipe_list, name='recipe_list'),
    url(r'^shoppinglist/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d\d?)$', 'recipeList.views.shopping_list', name='shoppinglist'),
    # Examples:
    # url(r'^$', 'recipes.views.home', name='home'),
    # url(r'^recipes/', include('recipes.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
