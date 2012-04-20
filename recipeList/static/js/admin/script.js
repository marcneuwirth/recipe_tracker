$(document).ready(function(){
	var $body = $('body');

	if($body.hasClass('recipeList-meal')){
		$('#id_recipe').chosen();
	}
	else if( $body.hasClass('recipeList-recipe')){
		$.getJSON('/ingredients.json', function(json){
			var ingredients = json.ingredients;

			$("#ingredient_set-group .name .vTextField").autocomplete({
				source: ingredients
			});
		});

		$('.unit select').chosen();
	}
});