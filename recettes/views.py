from django.shortcuts import render, get_object_or_404
from .models import Recipe, IngredientsList
from .forms import SelectRecipeForm, BatchCompositionForm


def index (request, recipe_id=''):
	recipes_list = Recipe.objects.all
	context = {'recipes_list': recipes_list}
		
	select_recipe_form = SelectRecipeForm(request.POST or None)
	batch_composition_form = BatchCompositionForm(request.POST or None)

	if select_recipe_form.is_valid():
		#selected_choice = question.choice_set.get(pk=request.POST['choice'])
		selected_recipe = Recipe.objects.get(pk=select_recipe_form.cleaned_data['recipe'])

	if batch_composition_form.is_valid():
		bread_qty = batch_composition_form.cleaned_data['bread_qty']
		bread_weight = batch_composition_form.cleaned_data['bread_weight']
		ingredients_list = IngredientsList.objects.filter(recipe=selected_recipe.id)
		ingredient_list_with_total=[]
		for item in ingredients_list:
			ingredient_list_with_total.append({
				'name': item.ingredient,
				'weight': item.weight_for_100g,
				'total': int(int(bread_qty) * int(bread_weight) * (item.weight_for_100g / 100)),
				'price_per_kg': item.ingredient.price_per_kg
				})
			
	return render(request, 'recettes/index.html', locals())

def detail (request, recipe_id):
	recipe = get_object_or_404(Recipe, pk=recipe_id)
	return render(request, 'recettes/details.html', {'recipe': recipe})