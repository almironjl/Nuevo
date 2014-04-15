
function cargar_video(valor){

           var params = "valor="+valor;

           var url = "/getvideourl_servicio/"+valor;
				$.ajax({
					   type: 'GET',
					   url: url,
					   dataType: 'html',
					   data: params,
					   beforeSend: function() {
                                           document.getElementById("ResultadoVideo").innerHTML= '<img src="'+ico_cargando+'" alt="img" width="300" height="300">';
						 },
                        		   complete: function() {
				
					   },
                                		   success: function(html) {
                                                       
                                                       
                                                        document.getElementById("ResultadoVideo").innerHTML= html;

                                                   }
					   });

}