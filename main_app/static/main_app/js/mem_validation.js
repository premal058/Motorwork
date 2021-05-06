$(document).ready(function(){

	$("#mem_sub").on("click",function()
	{
		var app_Name=$("#app_name").val();
        var nm_pat=/^[a-zA-Z ]+$/;
        if(app_Name=="")
        {
            $('#app_name_err').html("*Please enter Name.");
            
            return false;       
        }
        else if(!nm_pat.test(app_Name))
        {
            $('#app_name_err').html("*Please enter valid Name.");
            
            return false;          
        }
        else
        {
            $('#app_name_err').html("");
        }

         var app_Mail=$("#app_mail").val();
        var email_pat = /^([\w-\.]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([\w-]+\.)+))([a-zA-Z]{2,4}|[0-9]{1,3})(\]?)$/;
        if(app_Mail=="")
        {
            $('#app_mail_err').html("*Please enter EMail Address.");
            
            return false;       
        }
        else if(!email_pat.test(app_Mail))
        {
            $('#app_mail_err').html("*Please enter valid Email Address.");
            
            return false;          
        }
        else
        {
            $('#app_mail_err').html("");
        }


        var app_Phone=$('#app_phone').val();
        var phone_pat= /^\d{10}$/;
        if(app_Phone=="")
        {
            $('#app_phone_err').html("*Please enter Phone No.");
            
            return false;       
        }
        else if(!phone_pat.test(app_Phone))
        {
            $('#app_phone_err').html("*Please enter valid Phone No.");
            
            return false;          
        }
        else
        {
            $('#app_phone_err').html("");
        }

	});
});