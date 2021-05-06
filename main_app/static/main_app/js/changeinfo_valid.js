$(document).ready(function(){
    $('#infosub').on("click",function(){
        //alert('sss')
        var reg_Name=$("#ufn").val();
        var nm_pat=/^[a-zA-Z ]+$/;
        if(reg_Name=="")
        {
            $('#reg_name_err').html("*Please enter Name.");
            return false;       
        }
        else if(!nm_pat.test(reg_Name))
        {
            $('#reg_name_err').html("*Please enter valid Name.");
            return false;          
        }
        else
        {
            $('#reg_name_err').html("");
        }

        
        var reg_Phone=$('#up').val();
        var phone_pat= /^\d{10}$/;
        if(reg_Phone=="")
        {
            $('#reg_phone_err').html("*Please enter Phone No.");
           
            return false;       
        }
        else if(!phone_pat.test(reg_Phone))
        {
            $('#reg_phone_err').html("*Please enter valid Phone No.");
//registerForm.reg_phone.focus();
            return false;          
        }
        else
        {
            $('#reg_phone_err').html("");
        }        

        
        var reg_Add=$("#uadd").val();
        var add_pat=/^[0-9a-zA-Z,/ ]+$/;
        if(reg_Add=="")
        {
            $('#reg_add_err').html("*Please enter Address.");
         //   registerForm.reg_add.focus();
            return false;       
        }
        else if(!add_pat.test(reg_Add))
        {
            $('#reg_add_err').html("*Please enter valid Address.");
           // registerForm.reg_add.focus();
            return false;          
        }
        else
        {
            $('#reg_add_err').html("");
        }        

       
    });
});