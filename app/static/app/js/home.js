function initHome() {
	
	$(".combobox").focusin(function(e) {mostrarOpciones(e.currentTarget);});
	$(".combobox .seleccionado").click(function(e) {mostrarOpciones($(e.currentTarget).parent());});
	$(".combobox").focusout(function(e) {ocultarOpciones(e.currentTarget);});
	$(".combobox li").click(function(e) {seleccionarOpcionCombo($(e.currentTarget).parent().parent(),e.currentTarget);});
}
function seleccionarOpcionCombo(cmbElement, option) {
	$(cmbElement).find(".seleccionado").html($(option).html());
	ocultarOpciones(cmbElement);
	// falta seleccionar en el combo real
	$("#"+$(cmbElement).data("select")).val($(option).data("value"));
}
function mostrarOpciones(cmbElement) {
	$(cmbElement).find(".seleccionado").removeClass("onfocus");
	$(cmbElement).find(".seleccionado").removeClass("onchange");
	$(cmbElement).find(".seleccionado").addClass("onfocus");
	$(cmbElement).find(".opciones").css({display:"inline-block"});
}
function ocultarOpciones(cmbElement) {
	$(cmbElement).find(".seleccionado").removeClass("onfocus");
	$(cmbElement).find(".seleccionado").removeClass("onchange");
	$(cmbElement).find(".seleccionado").addClass("onchange");
	$(cmbElement).find(".opciones").css({display:"none"});
}
function mostrarVideo() {
    var tag = document.createElement('script');
    tag.src = "http://www.youtube.com/player_api";
    var firstScriptTag = document.getElementsByTagName('script')[0];
    firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);

    $(".layerVideo").fadeIn(500);
}
var videoPerfumes;
function onYouTubePlayerAPIReady() {
    videoPerfumes = new YT.Player('videoKunfood', {
        height: '100%',
        width: '100%',
        videoId: 'QnpmJ7XBhzY'
    });
}
function onPlayerReady(event) {
}
function onPlayerStateChange(event) {
}
function cerrarVideo(e) {
    videoPerfumes.stopVideo();
    $(".layerVideo").fadeOut(500);
}