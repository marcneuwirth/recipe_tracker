$(document).ready(function(){
	var $body = $('body');

	var chosen = function(selector){
		$('.form-row').not('.empty-form').find(selector).chosen();
	};

	if( $body.hasClass('recipeList-recipe')){
		$.getJSON('/ingredients.json', function(json){
			var ingredients = json.ingredients,
				autocomplete = function(){
					$("#ingredient_set-group .dynamic-ingredient_set .field-name .vTextField").autocomplete({
						source: function( request, response ) {
							var matcher = new RegExp( $.ui.autocomplete.escapeRegex( request.term ), "i" );
							response( $.grep( ingredients, function( value ) {
								value = value.label || value.value || value;
								return matcher.test( value );
							}).sort(function(a, b){
								return a.indexOf(request.term) > b.indexOf(request.term);
							}));
						},
						matchContains: false,
						delay: 0
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