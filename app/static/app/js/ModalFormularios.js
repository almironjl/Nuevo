function validateEmail(email) {
		var reg = /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
		return reg.test(email);
	}



	$(document).ready(function() {

		$(".modalbox").fancybox();
		$("#formregistro").submit(function() { return false; });
		$("#btnregistro").on("click", function(){
			var emailval  = $("#correo").val();
			var nomval    = $("#nombre").val();
			var apeval    = $("#apellidos").val();
			var pasval    = $("#password").val();
			var ckcond 	  = document.getElementById("ckb_condicion").checked;
			var rpasval   = $("#repit_password").val();
			var nomlen    = nomval.length;
			var apelen    = apeval.length;
			var paslen    = pasval.length;
			var rpaslen   = rpasval.length;
			var mailvalid = validateEmail(emailval);
			/*if(mailvalid == false) {	$("#correo").addClass("erroruser");	}

			else if(mailvalid == true){

				$("#correo").removeClass("erroruser");

			}

			

			if(paslen < 1) {	$("#password").addClass("errorpass"); $("#repit_password").addClass("errorpass");

			}

			else if(paslen >= 1){

				

				if(pasval != rpasval){				

					$("#password").addClass("errorpass");

					$("#repit_password").addClass("errorpass");

	

				}else if(pasval == rpasval){

					$("#password").removeClass("errorpass");

					$("#repit_password").removeClass("errorpass");

				}	

			}

			

			if(nomlen < 5) {

				$("#nombre").addClass("erroruser");

			}

			else if(nomlen >= 5){

				$("#nombre").removeClass("erroruser");

			}

			

			if(apelen < 5) {

				$("#apellidos").addClass("erroruser");

			}

			else if(apelen >= 5){

				$("#apellidos").removeClass("erroruser");

			}*/



			if(nomlen >= 4 && apelen >= 4 && ckcond == true && pasval == rpasval) {

				// if both validate we attempt to send the e-mail

				// first we hide the submit btn so the user doesnt click twice

				$("#btnregistro").before("<em id='msnRegister'>Procesando...</em>");
				$("#btnregistro").hide();

			

				$.ajax({

					type: 'POST',

					url: 'protected/extends/sendmessage.php',

					data: $("#formregistro").serialize(),

					success: function(dato) {

						if(dato == "true") {

							$("#formregistro").fadeOut("fast", function(){

								$(this).before("<p><strong>Success! Your register has been sent, thanks :)</strong></p>");

								setTimeout("$.fancybox.close()", 1000);
								location.reload();
							});

						}
						else
						{

								$("#formregistro").before("<p><strong>ERROR! El correo esta registrado, intentelo otra vez.</strong></p>");
								$("#msnRegister").hide();
								$("#btnregistro").show();
						}

					}

				});

			}

		});

	});





	$(document).ready(function() {

		var state;

		$("#showInitRegister").click(function (e) {

			e.preventDefault();

			state = $(this).attr("data-value");

			if(state == "false"){
				$("#contentInitSesion").hide();
				$("#ModalRegistroUsuario").show();
			}
			else
			 {
			 	$("#contentInitSesion").show();
				$("#ModalRegistroUsuario").hide();
			 }
		});


		$(".modalbox").fancybox();

		

		$("#formlogin").submit(function() { return false; });



		$("#btnlogin").on("click", function(){

			

			var corlval   = $("#correol").val();

			var paslval    = $("#passwordl").val();

			var ckrec 	  = document.getElementById("ckb_recordar").checked;



			var corllen    = corlval.length;

			var pasllen    = paslval.length;

			var mailvalid = validateEmail(corlval);



			if(corllen >= 5 && pasllen >= 5) {

				// if both validate we attempt to send the e-mail

				// first we hide the submit btn so the user doesnt click twice

				$("#btnprocesar").replaceWith("<p id='btnprocesar'><em>Procesando...</em><p>");

			

				$.ajax({

					type: 'POST',

					url: 'protected/extends/ExtendLoginKunfood.php?username='+corlval+"&password="+paslval,

					data: $("#formlogin").serialize(),

					success: function(data) {

						if(data == "true") {

							$("#formlogin").fadeOut("fast", function(){

								$(this).before("<p><strong>Exito, Ingreso Correctamente . gracias :)</strong></p>");

								setTimeout("$.fancybox.close()", 1000);

								//location.reload(true);

								var int=self.setInterval("refresh()",3000);

							});

						}else{

							$("#btnprocesar").replaceWith("<em>No esta registrado en kunfood...</em>");

						}

					}

				});

			}

		});

	});

	

	



function refresh()

 {

        location.reload(true);

 }









