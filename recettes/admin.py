from django.contrib import admin
from .models import Recipe
from .models import Ingredient
from .models import IngredientsList

admin.site.register(Recipe)
admin.site.register(Ingredient)
admin.site.register(IngredientsList)

