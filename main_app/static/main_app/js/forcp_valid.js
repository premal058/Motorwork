$(document).ready(function(){
    $('#csub').on("click",function(){
        //alert('sss')
         var reg_Pass1=$("#opass").val();
         var reg_Pass2=$("#npass").val();
        var pass_pat =  /^(?=.*[0-9])(?=.*[!@#$%^&*])[a-zA-Z0-9!@#$%^&*]{7,15}$/;                
        if(reg_Pass1=="")
        {
            $('#cp_opass_err').html("*Please enter Password.");
          
            return false;       
        }
        else if(!pass_pat.test(reg_Pass1))
        {
            $('#cp_opass_err').html("*Please enter Password in given format.");
          
            return false;          
        }
        else
        {
            $('#cp_opass_err').html("");
        }        
        if(reg_Pass2=="")
        {
            $('#cp_npass_err').html("*Please enter Password.");
          
            return false;       
        }
        else if(!pass_pat.test(reg_Pass2))
        {
            $('#cp_npass_err').html("*Please enter Password in given format.");
          
            return false;          
        }
        else
        {
            $('#cp_npass_err').html("");
        }        
        var reg_Cpass=$('#cpass').val();

        if(reg_Cpass=="")
        {
            $('#cp_cpass_err').html("*Please enter confirm Password.");
          
            return false;             
        }
        else if(reg_Cpass!=reg_Pass2)
        {
            $('#cp_cpass_err').html("*confirm Password and Password does not match.");
        
            return false;                
        }
        else
        {
            $('#cp_cpass_err').html("");
        }
       
    });
});