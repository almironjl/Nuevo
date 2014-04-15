function initGeneral() {

	$(".botonMostrar").click(function(e) {

		if ($(".contenidoPrincipal header .menuPrincipal nav").hasClass("visible")) {

			$(".contenidoPrincipal header .menuPrincipal nav").removeClass("visible");

		} else {

			$(".contenidoPrincipal header .menuPrincipal nav").addClass("visible");

		}

	});

}





function ValidarBusqueda(){

	

	var keyword = document.getElementById('keyword').value;

	

	if(keyword.length == 0){

		alert('hello');

         $("#AlertaBusqueda").css("display","inline");

	}else{

		alert("INGRESO");

	}

}



function redirec_detalles_rest(id,name, code, dish, type){

	//alert(id+" "+name);

	location.href = "Restaurant_general.php?id="+id+"&name="+name+"&code="+code+"&dish="+dish+"&type="+type;

}

			
function focusComment() {
	$("#comment").focus();
}


$(document).ready(function (argument) {
	var $formu;
	$("#form_comment").submit(function (e) {

		$formu = $(this);

		e.preventDefault();

		if($formu.attr('data-value')=="true") {

			if($("#comment").val() == "")
			{
				$("#comment").addClass("empty");	
				$("#comment").attr("placeholder","Ingrese un Comentario");
			}
			else 
			{
				$.ajax({
				        type: "POST",
				        url: "protected/extends/"+$formu.attr("action"),
				        data: $formu.serialize(),
				        success: function(datos){
				       		location.reload();
				      }	
				});
			}

		}
	});

	var tipo;

	$("#formrwish").submit(function (e) {
		e.preventDefault();

		$formu = $(this);

		$("#ModalWishList").find(".load_wish").show();
		$.ajax({
			        type: "POST",
			        url: "protected/extends/"+$formu.attr("action"),
			        data: $formu.serialize(),
			        success: function(datos){
			       		$("#ModalWishList").find(".load_wish").hide();
			       		
			       		tipo = $("#tipoModalProduct").val();

			       		$("#dish"+$("#ModalWishList").find(((tipo == '2')?".restaurantwish":".codedish")).val()).removeClass("wishlist_icon");
			       		$("#dish"+$("#ModalWishList").find(((tipo == '2')?".restaurantwish":".codedish")).val()).addClass("wishlist_icon_active");

			       		$.fancybox.close();
			      }	
			});
	});

});

function load_wish (codeUser, codeDish, nameDish, nameRest, isfavorite, commentWish, selectedDish, tipoProduct) {

	if(codeUser != "") 
	{
		//load value of forms
		$("#ModalWishList").find(".codedish").val(codeDish);
		$("#ModalWishList").find(".restaurantwish").val(nameRest);
		$("#ModalWishList").find("h3").text(nameDish);
		$("#tipoModalProduct").val((tipoProduct == '2')?"2":"1");
		$(".ListItem").hide();

		//load checkeds 

		if(selectedDish != ""){
			var selected = selectedDish.split(",");

			$("#listWishCreated .checks").attr("checked",false);

			for (var i = 0; i < selected.length; i++) {
				$("#listWishCreated .checks").each(function () {

					if($(this).is(":checked")==false)
					{
						if($(this).val() == selected[i] )
						{
							$(this).attr("checked",true);
						}
						else
						{
							$(this).attr("checked",false);
						}
					}
				});
			}

			//set text to label checked
			if(selected.length > 1)
			{
				$("#favorite").text(selected.length+" Wish List agregados");
			}
			else
			{
				if(selected.length == 1)
				{
					$("#favorite").text($("#listWishCreated .checks:checked").next().text());
					console.log($("#listWishCreated .checks:checked").next().text());
				}
			}
		}
		else
		{
			$("#favorite").text("Mi Wish List");
			$("#listWishCreated .checks").attr("checked",false);
		}

		//verify isset comment
		if(isfavorite)
		{
			$("#commentWish").val(commentWish);
		}
		else{
			$("#commentWish").val("");	
		}
	}

}
