$(document).ready(function(){
	var $body = $('body');

	var chosen = function(selector){
		$('.form-row').not('.empty-form').find(selector).chosen();
	};

	if( $body.hasClass('recipeList-recipe')){
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
		});
	}

	chosen('.field-unit select, .field-recipe select');

	$('body').on('click', '.add-row a', function(){
		console.log(this);
		chosen('.field-unit select, .field-recipe select');
	});
});