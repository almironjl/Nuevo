
function loginFace() {
 var url = '/me?fields=id,name,email';
    FB.login(function(response) {
        if (response.authResponse) {
  //if (response.session) {
            // connected
   //alert("ya esta conectado");
   myAPI();
        } else {
            // cancelled
   //alert("NO REALIZO LOGIN");
        }
    }, { perms: 'email' });
}

function myAPI() {
    FB.api('/me', function(response) {
  /*PROCESO AJAX PARA GUARDAR LOS DATOS QUE ENVIA FACEBBOK*/
        $.post('protected/extends/ExtendLoginFacebook.php', { accion: 'inicia', firstname: response.first_name,lastname: response.last_name , correo: response.email , id: response.id }, function(data) {
            //console.log('nombre:  ' + response.name + '.');
            //console.log('correo:  ' + response.email + '.');
            location.reload(true);
            //document.location.href = 'http://www.kunfood.com';
        });
    });
}

