$(document).ready(function(e) {
	var _srcI
	var _srcF
	$(".menu_left li:eq(0)").remove()
	
	//formulario
//	$(function(){
		// find all the input elements with title attributes
//		$('input[title!=""]').hint();
//		$('textarea[title!=""]').hint();
//	});
	
	$(".blur").hover(function(){
		$(this).attr('title','')
	});
	
	if($.browser.safari)
	{
		//alert(11)
	}
	
	
	$(".b_vo img:first").hide();

	
	$(".b_vo").toggle(function(e){
		e.preventDefault();
		$(".b_vo img:first").show();
		$(".b_vo img:last").hide();
		$(this).parent().parent().parent().animate({"bottom":"0px"},500);
		$("#slideraumentar").animate({"padding":"112px 0"},500);
		//$("#slideraumentar").css({"padding":"112px 0"});
		
	},function(){
		$(".b_vo img:last").show();
		$(".b_vo img:first").hide();
		$(this).parent().parent().parent().animate({"bottom":"-212px"},500);
		$("#slideraumentar").animate({"padding":"0 0"},500);
		//$("#slideraumentar").css({"padding":"0 0"});
	});
	
	$(".making_min").hover(function(){
		$(this).find(".c_hplay").hide();
	},function(){
		$(this).find(".c_hplay").show();
	});
	
	//subMenu
	$(".sub_menu").hide();
	$(".sub_menu li:last").css("background","none");
	$(".menu ul li:last").css("padding-left","0");
	
	if($.browser.msie && $.browser.version <= 8 || $.browser.chrome || $.browser.opera)
	{
		$(".menu ul li").css("padding-left","0px");
	}
	
	$(".hov").click(function(e){
		e.preventDefault();
	});
	
	//making
	$(".of").click(function(e){
		e.preventDefault();
		var ruta = 'making.php?KeepThis=true&TB_iframe=true&height=352&width=601';
		tb_show("MAKING OF", ruta, null, "");
	});
	
	//catalogo
	//var url = location.href;
	/*var href = $(location).attr('href');
	pat = /inicio/
	alert(pat.test(href))*/
	$(".catalogo").click(function(e){
		e.preventDefault();
		var ruta = 'catalogo.php?KeepThis=true&TB_iframe=true&height=572&width=766';
		tb_show("", ruta, null, _IDIOMA_GLOBAL_SUB_CATALOGO);
	});
});
