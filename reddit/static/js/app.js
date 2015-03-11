(function(){

    var app = {
        init: function() {

            $(".login").on("click", app.login);
            $(".register").on("click", app.register);
            $(".modal-error-close").on("click", app.modalErrorClose);
        },

        login: function(event){
            event.preventDefault();

            // hide errors div
            $(".username-login-errors").hide();
            $(".password-login-errors").hide();

            var loginRequest = $.post("/auth/login/", $("#loginForm").serialize());

            loginRequest.done(function(data){
                if( data.success === false ) {
                    app.showErrorMessages(data.loginf, "login");
                }
            });
        },

        modalErrorClose: function(event){
            event.preventDefault();

            $("#modal-auth-register").modal("show");
        },

        register: function(event){
            event.preventDefault();

            var registerRequest = $.post("/auth/register/", $("#registerForm").serialize());

            registerRequest.done(function(data){

                // close sign-in/register modal, open error modal and show message
                if( data.success == false && data.msg !== undefined ){
                    $("#modal-auth-register").modal("hide");
                    $(".text_error").html(data.msg);
                    $("#modal-error").modal("show");
                }

                if( data.success == false && data.msg === undefined) {
                    app.showErrorMessages(data.registerf, "register");
                }

                if( data.success == true ) {
                    window.location.reload();
                }
            });
        },

        showErrorMessages: function(objError, prefix){

            $.each(objError, function(key, val){
                var selector = "." + key + "-" + prefix + "-errors";
                $(selector).show();
                $(selector + " > .text-danger").html(val[0]);
            });

        },
    };

    $(document).ready(function() {
        app.init();
    });

})();
