<?php //restaurant_show.php 

require_once('class/classIndex.php');
require_once('class/classDistrito.php');
require_once('class/classAyuda.php');


$x = isset($_GET['x']) ? $_GET['x'] : "";
$activated = isset($_SESSION['sw_login']) ? $_SESSION['sw_login'] : "default";


$Distrito = new Distrito;
$Index = new index($activated);
$Ayuda = new Ayuda($activated); 


?>
<!DOCTYPE>
<html lang="es">
<head>
  

<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, user-scalable=yes, initial-scale=2">
<meta name="Keywords" content="Kunfood">
<meta name="Description" content="KUNFOOD permite ser atendido 'Al-toque' en restaurantes, bares. Navega por fotos de la carta, mira información de tus pedidos desde tu celular, permite al mozo brindar atención personalizada.">
<meta name="Title" content="Kunfood - Comunidad Gastronomica">
<meta name="Author" content="Kunfood">
<meta name="Subject" content="Comunidad Gastronomica">
<meta name="Generator" content="Kunfood">
<meta name="Language" content="es">
<meta name="Robots" content="index, follow">



<!-- MODEL-->

<link rel="stylesheet" href="model/reveal.css">

<script type="text/javascript" src="http://code.jquery.com/jquery-1.6.min.js"></script>
<script type="text/javascript" src="JS/video.js"></script>
<script type="text/javascript" src="model/jquery.reveal.js"></script>

<!--END MODEL-->		





<link rel="stylesheet" href="CSS/alert.css" type="text/css">

<link href="CSS/response.css" type="text/css" rel="stylesheet">

<link rel="stylesheet" type="text/css" href="CSS/general.css"/>

<link rel="stylesheet" type="text/css" href="CSS/login.css"/>

<script type="text/javascript" src="jquery-1.6.1.min.js"></script>

<script type="text/javascript" src="JS/scroll.js"></script>

<script src="JS/general.js" language="javascript" type="text/javascript"></script>
<script src="JS/home.js" language="javascript" type="text/javascript"></script>
<script src="JS/customSelect.js" type="text/javascript" language="javascript"></script>
<script src="JS/menu.js" type="text/javascript" language="javascript"></script>
<script src="JS/login.js" type="text/javascript" language="javascript"></script>

<link rel="stylesheet" href="CSS/video.css" type="text/css"/>

<script language="javascript" type="text/javascript">

$(document).ready(function(e) {
    initGeneral();
	initHome();

});

</script>





<link rel="stylesheet" href="JS/jquery_validate/css/validationEngine.jquery.css" type="text/css"/>
<script src="JS/jquery_validate/js/jquery-1.8.2.min.js" type="text/javascript"></script>
<script src="JS/jquery_validate/js/languages/jquery.validationEngine-en.js" type="text/javascript" charset="utf-8"></script>
<script src="JS/jquery_validate/js/jquery.validationEngine.js" type="text/javascript" charset="utf-8"></script>
<script>

		jQuery(document).ready(function(){
			// binds form submission and fields to the validation engine
			jQuery("#frm_registrar").validationEngine({autoHidePrompt:true});
		});

		/**
		*
		* @param {jqObject} the field where the validation applies
		* @param {Array[String]} validation rules for this field
		* @param {int} rule index
		* @param {Map} form options
		* @return an error string if validation failed
		*/

		function checkHELLO(field, rules, i, options){

			if (field.val() != "HELLO") {

				// this allows to use i18 for the error msgs

				return options.allrules.validate2fields.alertText;

			}

		}



</script>

 

        

<!-----------------VALIDAR NUMERO------------------>

<link rel="stylesheet" href="JS/jquery_validate/css/template.css" type="text/css"/>

<script src="JS/validar_numeric.jquery.js" type="text/javascript" ></script>

<script src="JS/validar_numeric.js" type="text/javascript" ></script>

<script src="JS/general.js" type="text/javascript" ></script>

<script type="text/javascript">

            $(function(){

                //Para escribir solo letras

                $('#miCampo1').validCampoFranz('abcdefghijklmnñopqrstuvwxyzáéiou');



                //Para escribir solo numeros    

                $('#dni').validCampoFranz('0123456789');    

            });

        </script>  

<!------------------------------------------------>



<!-- MOSTRAR MODEL AYUDA -->

<link rel="stylesheet" href="CSS/modelAyuda.css" type="text/css"/>

<script src="JS/modelAyuda.js" type="text/javascript"></script>

<!-- END MODEL AYUDA  -->

    



<!-- CONECTARME CON FACEBOOK -->

<script src="//connect.facebook.net/en_US/all.js"></script>

<script src="JS/facebook.js" type="text/javascript"></script>

<!--END FACEBOOK -->





<title>Kunfood - Vive tu Experiencia Kunfood</title>

</head>



<body>



<div id="fb-root"></div>



<script>(function(d, s, id) {



  var js, fjs = d.getElementsByTagName(s)[0];

  if (d.getElementById(id)) return;

  js = d.createElement(s); js.id = id;

  js.src = "//connect.facebook.net/es_LA/all.js#xfbml=1&appId=338384736288835";

  fjs.parentNode.insertBefore(js, fjs);

}(document, 'script', 'facebook-jssdk'));</script>



<script>



  // Additional JS functions here

  window.fbAsyncInit = function() {

    FB.init({

      appId      : '338384736288835', // App ID

      channelUrl : 'http://www.kunfood.com', // Channel File

      status     : true, // check login status

      cookie     : true, // enable cookies to allow the server to access the session

      xfbml      : true  // parse XFBML

	   });









  };



</script>



<div class="contenidoPrincipal">



<!--SCREEN MODAL-->

<?php include_once('contenidolvidepass.php'); ?>
<?php include_once('contenidoregistro.php'); ?>
<?php include_once('contenidologin.php'); ?>
<input type="hidden" name="x" id="x" value="<?php echo $x ?>">
<!--END SCREEN MODAL-->

<script>

MensajeAlerta();

</script>

    <header>



    	<div class="menuPrincipal">



            <a class="logo"  href="index.php"><h1 title="Kunfood - Inicio">Kunfood</h1></a>

           



            <nav>



                <ul>

                    <!--

                     <a href="#"  onclick="Construir();" title="Top Restaurantes"><li><table><tr><td>Top restaurants</td></tr></table></li></a>

                   <a href="delivery.php" title="Haz tu delivery"><li><table><tr><td>Delivery</td></tr></table></li></a>

                    <a href="reservar.php" title="Reservar"><li><table><tr><td>Reservas</td></tr></table></li></a>

                    <span id="notic">

                    <a href="#noticiax"  title="Las últimas noticias">

                        <li><table><tr><td>Kunfood noticias</td></tr></table></li>

                    </a>

                    </span>

                    -->
			  <a href="experiencia-kunfood.php" title="Vive la Experiencia Kunfood!"><li><table><tr><td>Experiencia Kunfood</td></tr></table></li></a>


                    <a href="#" id="showlogin" title="AYUDA"><li><table><tr><td>Ayuda</td></tr></table></li></a>

              
                    <!--MENU AYUDA -->

                        <div id="loginpanel" style="display:none; position: absolute">

                         <?php $Ayuda ->menuAyuda(); ?>

			</div>

                    <!-- END MENU AYUDA -->

                    

                    <li class="registro">

                        <!-- Si no está logueado -->

                        <table width="125%" height="103%">

                        /<tr><td>



                            <?php 	$Index->ValidarSession(); ?>

                            <div id="cambiar"> 

                            <table cellpadding="0" width="183%" height="103%" cellspacing="0">

                                    <tr>

                                    <td width="100%">

                                    <?php echo $Index->setUser(); ?><?php echo  $Index->setImg() ?>

	    			    </td>

                                    </tr>

                                    <tr>

                                    <td>

                                    <?php echo $Index->setSalir() ?>

                                    </td>

                                    </tr>

                                 

                             </table>

                             </div>

        					 <!--<a href="#" onclick="javascript:mostrarRegistro();" title="Regístrate al toque!">Regístrate</a>-->

			                 <!--<a href="#" onclick="javascript:mostrarInicioSesion();" title="Inicia sesión">Inicia Sesión</a>-->



                        </td></tr></table>



                        <!-- Si está logueado -->



                    </li>



                </ul>



            </nav>



            <div class="botonMostrar"></div>



        </div>



  



    </header>


<section id="container">
<script>

MensajeAlerta();

</script>
<?php if($x == 'c'){ ?>

<div class="alerta mensajes">No existe ninguna cuenta asociada a EMAIL. Puede que te registraras usando una dirección de correo electrónico diferente o incorrecta.</div>

<?php } ?>
<article id="conteinervideo">
<table width="950" height="500" border="0" cellpadding="0" cellspacing="0" style="box-shadow:5px 5px 10px rgba(0,0,0,0.5);border-radius:6px !important;">
  <tr>
      <td width="510" height="20" background="IMAGENES/pie-video.png"><span class="kunfood">Kunfood</span> <span class="titexp">Vive la Experiencia</span></td>
      <td width="184" background="IMAGENES/pie-video.png"><span class="titlista">Lista:</span></td>
  </tr>
  <tr>
    <td height="280" bgcolor="#333333">
        
        <!-- ------------------->
        <div id="ResultadoVideo">
            <iframe width="100%" height="400px" src="http://www.youtube.com/embed/FgO1ZLweYyI" frameborder="0" allowfullscreen></iframe>
        </div>
        <!-- ------------------->
        
    </td>
    <td width="270px" class="listVideo">
        
        <!-- ------------------->
        <table width="100%" height="100%" border="0">
            <tr>
              <td class="border-botton" onclick="cargar_video('1')">
                  <img class='nav-thumb' height='50px' width='68px' src="http://img.youtube.com/vi/FgO1ZLweYyI/1.jpg" />
              </td>
              <td class="border-botton" onclick="cargar_video('1')"><span class="titulo">Nguyen Chavez</span></td>
            </tr>
            <tr>
              <td class="border-botton" onclick="cargar_video('2')">
                  <img class='nav-thumb'  height='50px' width='68px' src="http://img.youtube.com/vi/XvNNvaAgbZU/2.jpg"/>
              </td>
               <td class="border-botton" onclick="cargar_video('2')"><span class="titulo">Martin Morales</span></td>
            </tr>
            <tr>
              <td class="border-botton" onclick="cargar_video('3')">
                  <img class='nav-thumb' height='50px' width='68px' src="http://img.youtube.com/vi/y1ryZqZZlTs/3.jpg"/>
              </td>
               <td class="border-botton" onclick="cargar_video('3')"><span class="titulo">Jose Luis Cordeiro</span></td>
            </tr>
            <tr>
              <td class="border-botton" onclick="cargar_video('4')">
                  <img class='nav-thumb' height='50px' width='68px' src="http://img.youtube.com/vi/6V9aDf992gs/1.jpg"/>
              </td>
               <td class="border-botton" onclick="cargar_video('4')"><span class="titulo">Martin Morales</span></td>
            </tr>
          </table>
        <!-- ------------------->
        
    </td>
  </tr>
  <tr>
    <td height="20" background="IMAGENES/pie-video.png">&nbsp;</td>
    <td height="20" background="IMAGENES/pie-video.png">&nbsp;</td>
    </tr>
</table>
<article>

</section>

<section id="containerExperiencia">
    <br>
    <table width="805" border="0" align="center" class="tablaExperiencia" cellpadding="0" cellspacing="0" style="box-shadow:5px 5px 10px rgba(0,0,0,0.5);border-radius:6px !important;">
  <tr> 
      <td colspan="4" class="titleExp">Y a ti dónde te Gustaria vivir la Experiencia Kunfood!!</td>
  </tr>
  <tr>
      <td width="75"><span class="titexp2">Nombre de Restaurante</span></td>
    <td width="144">
    
      <input type="text" class="textexp" placeholder="Ingresar Nombre" name="textfield" id="textfield">
    </td>
    <td width="4">&nbsp;</td>
    <td width="154" rowspan="2">
        <input type="submit" name="button" class="btnexp"  id="button" value="Enviar">
	</td>
  </tr>
  <tr>
    <td><span class="titexp2">Correo Electrónico</span> </td>
    <td>
     
        <input type="text"  class="textexp" placeholder="Ingresar email" name="textfield2" id="textfield2">
    </td>
    <td>&nbsp;</td>
  </tr>
</table>                                               
    <br>
<br>
</section>
     

<section class="descargaAplicacion">

    	<div class="fondoMadera">

        	<div class="contenido">

                <hgroup>

                    <h1>Descarga nuestra  aplicación para móbiles.</h1>

                    <h2>Mejora tu experiencia gastronómica <a href="javascript:mostrarVideo();">Ver video</a></h2>

                </hgroup>

                <p>KUNFOOD permite ser atendido "Al-toque" en restaurantes, bares. Navega por fotos de la carta, mira información de tus pedidos desde tu celular, permite al mozo brindar atención personalizada.</p>

                <div class="botonesDescarga">



                	<a class="mac" target="_blank" href="https://itunes.apple.com/pe/app/kunfood/id653978440?l=en&mt=8"></a>

                	<a class="android" target="_blank" href="https://play.google.com/store/apps/details?id=com.seinc.kunfood&hl=es"></a>

                </div>

                <div class="imagen" onClick="javascript:mostrarVideo();">

                    <img src="IMAGENES/App_gratis_ver_video.png" alt="Aplicación Kunfood"/>

                </div>



            </div>



        </div>

        <div class="layerVideo">

        	<div class="player" id="videoKunfood">

            	

            </div>

            <div class="btnCerrar" onClick="javascript:cerrarVideo();">Cerrar X</div>

        </div>

    </section>

   


    <footer>
    	<div>
        	<a class="logoFooter" href="index.php"></a>
            <nav>
            	<a href="ayuda.php">Ayuda</a>
            	<a href="politicas.php">Política y Privacidad</a>
            	<a href="mapa.php">Mapa del sitio</a>
            </nav>
        </div>
    </footer>
</div>
</body>
</html>



<!-----------------POPUP------------------>  

<link rel="stylesheet" type="text/css" href="CSS/estilos.css" media="all" />

<script language="javascript" type="text/javascript" src="JS/csspopup.js"></script>

<!-----------------END POPUP------------------>