$(document).ready(function(){
	var $body = $('body');

	if($body.hasClass('recipeList-meal')){
		$('#id_recipe').chosen();
	}
	else if( $body.hasClass('recipeList-recipe')){
		$.getJSON('/ingredients.json', function(json){
			var ingredients = json.ingredients;

			var autocomplete = function(){
				$("#ingredient_set-group .dynamic-ingredient_set .field-name .vTextField").autocomplete({
					source: ingredients
				});
			};

			$('.add-row a').on('click', function(){
				autocomplete();
			});
			autocomplete();

			$('.dynamic-ingredient_set .field-unit select').chosen();

			$('.add-row a').on('click', function(){
				$('.dynamic-ingredient_set .field-unit select').chosen();
			});
		});
	}
});