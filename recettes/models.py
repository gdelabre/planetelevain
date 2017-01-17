from django.db import models

class Ingredient(models.Model):
	name = models.CharField(max_length=200)
	price_per_kg = models.DecimalField(max_digits=5, decimal_places=2)
	
	def __str__(self):
		return self.name

class Recipe(models.Model):
	name = models.CharField(max_length=200)
	description = models.TextField()
	ingredients = models.ManyToManyField(Ingredient, through='IngredientsList')

	def __str__(self):
		return self.name

class IngredientsList(models.Model):
	recipe = models.ForeignKey(Recipe)
	ingredient = models.ForeignKey(Ingredient)
	weight_for_100g = models.IntegerField()

	def __str__(self):
		return "{0}: {2}g de {1}".format(self.recipe, self.ingredient, self.weight_for_100g)


