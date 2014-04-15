function validateEmail($email) {
    var emailReg = /^([\w-\.]+@([\w-]+\.)+[\w-]{2,4})?$/;
    if (!emailReg.test($email)) {
        return false;
    } else {
        return true;
    }
}


function MensajeAlerta() {
    x = document.getElementById('x').value;

    if (x == 'c') {
        $(document).ready(function () {
            setTimeout(function () {
                $(".mensajes").fadeOut(800).fadeIn(800).fadeOut(500).fadeIn(500).fadeOut(300);
            }, 3000);
        });
    }
}
function create_token() {
    var text = "";
    var possible = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";

    for (var i = 0; i < 10; i++)
        text += possible.charAt(Math.floor(Math.random() * possible.length));

    return text;
}

function RegistrarRestaurant() {
//    $('#btn_register').attr("disabled", "disabled");
    var emailx = document.getElementById('emailWebSite').value;
    var telefonox = document.getElementById('telefono').value;
    var inicx = document.getElementById('inic').value;
    var namex = document.getElementById('name').value;
    var addressx = document.getElementById('address').value;
    var websitex = document.getElementById('website').value;
    var createtoken = create_token();

    if (emailx.length != 0 && telefonox.length != 0 && inicx.length != 0 && namex.length != 0 && addressx.length != 0) {

        if (validateEmail(emailx) != true) {
//             alert('ingrese correo valido');
            $("#emailWebSite").val('');
            $("#emailWebSite").focus();
            $("#emailWebSite").css("box-shadow", "0px 0px 10px red");

            if (telefonox.length == 0) $("#telefono").css("box-shadow", "0px 0px 10px red"); else $("#telefono").css("box-shadow", "5px 5px 10px rgba(0,0,0,0.5)");
            if (inicx.length == 0) $("#inic").css("box-shadow", "0px 0px 10px red"); else $("#inic").css("box-shadow", "5px 5px 10px rgba(0,0,0,0.5)");
            if (namex.length == 0) $("#name").css("box-shadow", "0px 0px 10px red"); else $("#name").css("box-shadow", "5px 5px 10px rgba(0,0,0,0.5)");
            if (addressx.length == 0) $("#address").css("box-shadow", "0px 0px 10px red"); else $("#address").css("box-shadow", "5px 5px 10px rgba(0,0,0,0.5)");

            $("#info").css("display", "block");
            setTimeout(function () {
                $("#info").fadeOut(800).fadeIn(800).fadeOut(500).fadeIn(500).fadeOut(300);
            }, 3000);
        } else {

            //alert('INGRESO A FUNCION;'+emailx+'/'+telefonox+'/'+inicx+'/'+namex+'/'+addressx+'/'+websitex);

            var csrfmiddlewaretoken = $('[name="csrfmiddlewaretoken"]').val();
            $.post("/restaurant_registro/",
                {
                    email: emailx,
                    phone: telefonox,
                    inicial: inicx,
                    nombre: namex,
                    address: addressx,
                    website: websitex,
                    confirmation_token: createtoken,
                    status : 0,
                    'csrfmiddlewaretoken': csrfmiddlewaretoken }
                , function (data) {

                    if (data == 0) {
                        //alert('no existe');

                        $("#emailWebSite").css("box-shadow", "none");
                        if (emailx.length == 0) $("#emailWebSite").css("box-shadow", "0px 0px 10px red"); else $("#emailWebSite").css("box-shadow", "5px 5px 10px rgba(0,0,0,0.5)");
                        if (telefonox.length == 0) $("#telefono").css("box-shadow", "0px 0px 10px red"); else $("#telefono").css("box-shadow", "5px 5px 10px rgba(0,0,0,0.5)");
                        if (inicx.length == 0) $("#inic").css("box-shadow", "0px 0px 10px red"); else $("#inic").css("box-shadow", "5px 5px 10px rgba(0,0,0,0.5)");
                        if (namex.length == 0) $("#name").css("box-shadow", "0px 0px 10px red"); else $("#name").css("box-shadow", "5px 5px 10px rgba(0,0,0,0.5)");
                        if (addressx.length == 0) $("#address").css("box-shadow", "0px 0px 10px red"); else $("#address").css("box-shadow", "5px 5px 10px rgba(0,0,0,0.5)");
                        $("#exito").css("display", "block");
                        setTimeout(function () {
                            $("#exito").fadeOut(800).fadeIn(800).fadeOut(500).fadeIn(500).fadeOut(300);
                        }, 3000);
                        setTimeout("DireccionHome()", 7000);

                    } else {
                        //alert('ya esta registrado!');

                        $("#emailWebSite").css("box-shadow", "0px 0px 10px red");
                        if (telefonox.length == 0) $("#telefono").css("box-shadow", "0px 0px 10px red"); else $("#telefono").css("box-shadow", "5px 5px 10px rgba(0,0,0,0.5)");
                        if (inicx.length == 0) $("#inic").css("box-shadow", "0px 0px 10px red"); else $("#inic").css("box-shadow", "5px 5px 10px rgba(0,0,0,0.5)");
                        if (namex.length == 0) $("#name").css("box-shadow", "0px 0px 10px red"); else $("#name").css("box-shadow", "5px 5px 10px rgba(0,0,0,0.5)");
                        if (addressx.length == 0) $("#address").css("box-shadow", "0px 0px 10px red"); else $("#address").css("box-shadow", "5px 5px 10px rgba(0,0,0,0.5)");

                        $("#alerta").css("display", "block");
                        setTimeout(function () {
                            $("#alerta").fadeOut(800).fadeIn(800).fadeOut(500).fadeIn(500).fadeOut(300);
                        }, 3000);
                        $('#btn_register').removeAttr("disabled");
                    }
                });

        }//END VALIDAR EMAIL

    } else {
        // alert('Ingrese los campos que faltan!');

        if (emailx.length == 0) {
            $("#emailWebSite").css("box-shadow", "0px 0px 10px red");
        } else {
            $("#emailWebSite").css("box-shadow", "5px 5px 10px rgba(0,0,0,0.5)");
        }
        if (telefonox.length == 0) $("#telefono").css("box-shadow", "0px 0px 10px red"); else $("#telefono").css("box-shadow", "5px 5px 10px rgba(0,0,0,0.5)");
        if (inicx.length == 0) $("#inic").css("box-shadow", "0px 0px 10px red"); else $("#inic").css("box-shadow", "5px 5px 10px rgba(0,0,0,0.5)");
        if (namex.length == 0) $("#name").css("box-shadow", "0px 0px 10px red"); else $("#name").css("box-shadow", "5px 5px 10px rgba(0,0,0,0.5)");
        if (addressx.length == 0) $("#address").css("box-shadow", "0px 0px 10px red"); else $("#address").css("box-shadow", "5px 5px 10px rgba(0,0,0,0.5)");
        $("#error").css("display", "block");
        setTimeout(function () {
            $("#error").fadeOut(800).fadeIn(800).fadeOut(500).fadeIn(500).fadeOut(300);
        }, 3000);

    }
}


function DireccionHome() {
    location.href = '/';

}
