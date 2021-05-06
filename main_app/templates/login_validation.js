$(document).ready(function(){
    $('#sub').on("click",function(){

        var mail=$('#login_mail').val();
        var pass=$('#login_pass').val();
        var role=$('#login_role').val();
        
        if(role=="Role")
        {
            $('#login_role_err').html("*Please select Role.");
            login.login_role.focus();
            //alert('role');
            return false;   
            alert('role'); 
        }
       if(role!="Role")
        {
               $('#login_role_err').html("");
        }


        var mail_pat = /^([\w-\.]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([\w-]+\.)+))([a-zA-Z]{2,4}|[0-9]{1,3})(\]?)$/;
        if(mail=="")
        {
            $('#login_mail_err').html("*Please enter Email Address.");   
            return false;    
        }
        else if(!mail_pat.test(mail))
        {
            $('#login_mail_err').html("*Please enter proper Email Address.");
            login.login_mail.focus();
            //alert('role');
            return false;    
        }
        if(mail_pat.test(mail))
        {
            $('#login_mail_err').html("");
        }


        var pass_pat =  /^(?=.*[0-9])(?=.*[!@#$%^&*])[a-zA-Z0-9!@#$%^&*]{7,15}$/;
        if(pass_pat.test(pass))
        {
            $('#login_pass_err').html("");
        }
        if(pass=="")
        {
                $('#login_pass_err').html("*please enter password");    
                return false;    
        }
        else if(!pass_pat.test(pass))
        {
            $('#login_pass_err').html("*Password should be of 7 to 15 characters with at least one numeric digit and a special character");
            login.login_pass.focus();
            //alert(pass);
            return false;    
        }
    });


    $('#reg_sub').on("click",function(){

        var reg_Role=$('#reg_role').val();
        
        if(reg_Role=="Role")
        {
            $('#reg_role_err').html("*Please select Role.");
            registerForm.reg_role.focus();
            return false;    
        }
        else
        {
            $('#reg_role_err').html("");
        }

        var reg_Name=$("#reg_name").val();
        var nm_pat=/^[a-zA-Z]+$/;
        if(reg_Name=="")
        {
            $('#reg_name_err').html("*Please enter Name.");
            registerForm.reg_name.focus();
            return false;       
        }
        else if(!nm_pat.test(reg_Name))
        {
            $('#reg_name_err').html("*Please enter valid Name.");
            registerForm.reg_name.focus();
            return false;          
        }
        else
        {
            $('#reg_name_err').html("");
        }

        var reg_Add=$("#reg_add").val();
        var add_pat=/^[0-9a-zA-Z,/ ]+$/;
        if(reg_Add=="")
        {
            $('#reg_add_err').html("*Please enter Address.");
            registerForm.reg_add.focus();
            return false;       
        }
        else if(!add_pat.test(reg_Add))
        {
            $('#reg_add_err').html("*Please enter valid Address.");
            registerForm.reg_add.focus();
            return false;          
        }
        else
        {
            $('#reg_add_err').html("");
        }        

        var reg_Phone=$('#reg_phone').val();
        var phone_pat= /^\d{10}$/;
        if(reg_Phone=="")
        {
            $('#reg_phone_err').html("*Please enter Phone No.");
            registerForm.reg_phone.focus();
            return false;       
        }
        else if(!phone_pat.test(reg_Phone))
        {
            $('#reg_phone_err').html("*Please enter valid Phone No.");
            registerForm.reg_phone.focus();
            return false;          
        }
        else
        {
            $('#reg_phone_err').html("");
        }        

        var reg_Mail=$("#reg_mail").val();
        var email_pat = /^([\w-\.]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([\w-]+\.)+))([a-zA-Z]{2,4}|[0-9]{1,3})(\]?)$/;
        if(reg_Mail=="")
        {
            $('#reg_mail_err').html("*Please enter Address.");
            registerForm.reg_mail.focus();
            return false;       
        }
        else if(!email_pat.test(reg_Mail))
        {
            $('#reg_mail_err').html("*Please enter valid Email Address.");
            registerForm.reg_mail.focus();
            return false;          
        }
        else
        {
            $('#reg_mail_err').html("");
        }

        var reg_Pass=$("#reg_pass").val();
        var pass_pat =  /^(?=.*[0-9])(?=.*[!@#$%^&*])[a-zA-Z0-9!@#$%^&*]{7,15}$/;                
        if(reg_Pass=="")
        {
            $('#reg_pass_err').html("*Please enter Password.");
            registerForm.reg.pass.focus();
            return false;       
        }
        else if(!pass_pat.test(reg_Pass))
        {
            $('#reg_pass_err').html("*Please enter Password in given format.");
            registerForm.reg_pass.focus();
            return false;          
        }
        else
        {
            $('#reg_pass_err').html("");
        }        

        var reg_Cpass=$('#reg_cpass').val();

        if(reg_Cpass=="")
        {
            $('#reg_cpass_err').html("*Please enter confirm Password.");
            registerForm.reg_cpass.focus();
            return false;             
        }
        else if(reg_Cpass!=reg_Pass)
        {
            $('#reg_cpass_err').html("*confirm Password and Password does not match.");
            registerForm.reg_cpass.focus();
            return false;                
        }
        else
        {
            $('#reg_cpass_err').html("");
        }
    });
});