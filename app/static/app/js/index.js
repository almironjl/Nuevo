function cambiarTextMapa() {
	//alert('HELLo');
	var r = document.getElementById('hid').value;
	if (r == '1') {
		//document.getElementById('titmap').innerHTML = 'Ocultar mapa';
		//$("#mapcanvas").css({'width':'100%','height':'140px','transition-duration':'.5s'});
		$("#area-selection").css({
			'height': '260px',
			'transition-duration': '.5s'
		});
		//$("#MapForm").css({'visibility':'visible','height':'0px','transition-duration':'.5s'});
		document.getElementById('hid').value = '2';
	} else {
		//document.getElementById('titmap').innerHTML = 'Ver mapa';
		$("#area-selection").css({
			'height': '100px',
			'transition-duration': '.5s'
		})
		//$("#mapcanvas").css({'width':'100%','height':'0px','transition-duration':'.5s'});
		//$("#MapForm").css({'visibility':'hidden','height':'140px','transition-duration':'.5s'});
		document.getElementById('hid').value = '1';
	}
}

function refresh() {
	location.reload(true);
}

function Cambiar_Idioma_Web() {
	//var int=self.setInterval("refresh()",8000);
	var idioma = document.getElementById('idioma_web').value;
	//alert(idioma);
	$.post('protected/extends/ExtendIdiomaWeb.php', {
		idiomaweb: idioma
	}, function (data) {
		location.reload(true);
	});
}

function Destroy_session() {
	//alert(idioma);
	$.post('protected/extends/ExtendDestroyFacebook.php', {
		idiomaweb: 'test'
	}, function (data) {
		location.reload(true);
	});
}

function Search_Lists_Restaurant() {
	var keyval = $("#keyword").val();
	var lugval = $("#area-selector").val();
	var keylen = keyval.length;
    var luglen = lugval.length;
	if(keylen==0) keyval="*";
    if(luglen==0) lugval="*";
	if (keylen == 0 && luglen == 0) {
		$("#AlertaBusqueda").css("display", "inline");
	} else {
		//alert('ingreso');
		$("#AlertaBusqueda").css("display","none");
		location.href = "/busqueda/"+keyval+"/"+lugval;
	}
}

function Cargar_restaurantes(pag) {
	//alert("hola mundo");
	var key_h = document.getElementById('hidden-keyword').value;
	var pla_h = document.getElementById('hidden-lugar').value;
	//alert('hola');
	Mostrar_Restaurants(pla_h, key_h, pag);
	Mostrar_Map(pla_h, key_h, pag);
}

function Cargar_restaurantesBuscar() {
	//alert("hola mundo");
	var key = document.getElementById('keyword').value;
	var pla = document.getElementById('area-selector').value;
	Mostrar_Restaurants(pla, key, 1);
	Mostrar_Map(pla, key, 1);
}

function Cargar_restaurantesBuscarFiltro() {
	document.getElementById('filtrox').innerHTML = 'Ubicacion';
	//alert("hola mundo");
	var key = document.getElementById('keyword').value;
	var pla = document.getElementById('area-selector').value;
	//var ledist = document.getElementById('ckdlugar').length;
	//alert(ledist);
	var x = 1838;
	var y = -1;
	var ArrId = new Array();
	var ArrStat = new Array();
	for (i = 1838; i < 1869; i++) {
		x++;
		y++;
		var ckid = document.getElementById('ckd' + x).value;
		var ckstat = document.getElementById('ckd' + x).checked;
		if (ckstat == true) {
			ArrId[y] = ckid;
			ArrStat[y] = ckstat;
		}
		//alert(ckid+" "+ckstat)
		//alert("holaaaaaa");
	}
	/* for(a=0;a<30;a++){
        if(ArrIdx[a] == "" && ArrStatx[a] == ""){
        }else{
            ArrId[a] = ArrIdx[a] ;
            ArrStat[a] = ArrStat[a];
        }
     }
 	*/
	//alert(ArrId);
	//alert(ArrStat);
	// Ubicacion,T. Comida
	Mostrar_RestaurantsFilt(pla, key, 1, ArrId, ArrStat);
	Mostrar_MapFilt(pla, key, 1, ArrId, ArrStat);
}

function Mostrar_RestaurantsFilt(pla, key, pag, arrid, arrstat) {
	var params = "keyword=" + key + "&lugar=" + pla + "&pagina=" + pag + "&arrid=" + arrid + "+&arrstat=" + arrstat;
	var url = "protected/extends/ExtendListarRestaurant.php";
	$.ajax({
		type: 'POST',
		url: url,
		dataType: 'html',
		data: params,
		beforeSend: function () {
			document.getElementById("listings-restaurant").innerHTML = '<img style="margin: 0 auto !important;" src="images/cargando.gif" alt="img" width="100%" height="100%">';
		},
		complete: function () {},
		success: function (html) {
			document.getElementById("listings-restaurant").innerHTML = html;
		}
	});
}

function Mostrar_MapFilt(pla, key, pag, arrid, arrstat) {
	var params = "keyword=" + key + "&lugar=" + pla + "&pagina=" + pag + "&arrid=" + arrid + "+&arrstat=" + arrstat;
	var url = "protected/extends/ExtendMostrarMap.php";
	$.ajax({
		type: 'POST',
		url: url,
		dataType: 'html',
		data: params,
		beforeSend: function () {
			document.getElementById("map-canvas").innerHTML = '<img src="images/cargando.gif" alt="img" width="100%" height="100%">';
		},
		complete: function () {},
		success: function (html) {
			document.getElementById("map-canvas").innerHTML = html;
			//if(html=="success"){
			//window.location = "index.php"
			// }
		}
	});
}

function Mostrar_Restaurants(pla, key, pag) {
	var params = "keyword=" + key + "&lugar=" + pla + "&pagina=" + pag;
	var url = "protected/extends/ExtendListarRestaurant.php";
	$.ajax({
		type: 'POST',
		url: url,
		dataType: 'html',
		data: params,
		beforeSend: function () {
			document.getElementById("listings-restaurant").innerHTML = '<img style="margin: 0 auto !important;" src="images/cargando.gif" alt="img" width="100%" height="100%">';
		},
		complete: function () {},
		success: function (html) {
			document.getElementById("listings-restaurant").innerHTML = html;
			//if(html=="success"){
			//window.location = "index.php"
			// }
		}
	});
}

function Mostrar_Map(pla, key, pag) {
	var params = "keyword=" + key + "&lugar=" + pla + "&pagina=" + pag;
	var url = "protected/extends/ExtendMostrarMap.php";
	$.ajax({
		type: 'POST',
		url: url,
		dataType: 'html',
		data: params,
		beforeSend: function () {
			document.getElementById("map-canvas").innerHTML = '<img src="images/cargando.gif" alt="img" width="100%" height="100%">';
		},
		complete: function () {},
		success: function (html) {
			document.getElementById("map-canvas").innerHTML = html;
			//if(html=="success"){
			//window.location = "index.php"
			// }
		}
	});
}