$(document).ready(function(){
    $('#pass_sub').on("click",function(){

        
        var pass=$('#c_pass').val();
        var cpass=$('#c_cpass').val();
        var otp = $("#potp").val();

        if(otp=="")
        {
            $('#c_otp_err').html("*please enter OTP");    
            return false;       
        }
        else
        {
            $('#c_otp_err').html("");    
        }
        var pass_pat =  /^(?=.*[0-9])(?=.*[!@#$%^&*])[a-zA-Z0-9!@#$%^&*]{7,15}$/;
        if(pass_pat.test(pass))
        {
            $('#c_pass_err').html("");
        }
        if(pass=="")
        {
                $('#c_pass_err').html("*please enter password");    
                return false;    
        }
        else if(!pass_pat.test(pass))
        {
            $('#c_pass_err').html("*Password should be of 7 to 15 characters with at least one numeric digit and a special character");
            //alert(pass);
           return false;    
        }

        if(cpass=="")
        {
            $('#c_cpass_err').html("*Please enter confirm Password.");
            return false;             
        }
        else if(cpass!=pass)
        {
            $('#c_cpass_err').html("*confirm Password and Password does not match.");
            return false;                
        }
        else
        {
            $('#c_cpass_err').html("");
        }
    });

});