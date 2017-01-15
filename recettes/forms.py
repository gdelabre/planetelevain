from django import forms
from .models import Recipe

class SelectRecipeForm(forms.Form):
	recipe = forms.ChoiceField(widget=forms.Select(attrs={"onChange":'this.form.submit()'}), choices=Recipe.objects.all().values_list('pk', 'name'), required=True, label="Recette")

class BatchCompositionForm(forms.Form):
	bread_qty = forms.ChoiceField(choices=[(a,b) for a,b in zip(range(1,101),range(1,101))], required=True, label="Nombre de pains ")
	bread_weight = forms.ChoiceField(choices=[(a,b) for a,b in zip(range(100,2100,100),range(100,2100,100))], required=True, label="Poids")

class RecipeForm(forms.ModelForm):
	class Meta:
		model = Recipe
		fields = "__all__"
