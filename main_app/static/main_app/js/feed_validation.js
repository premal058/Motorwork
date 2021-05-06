$(document).ready(function(){

	$("#feed_sub").on("click",function(){

		var msg = $("#feed_msg").val();
		var email = $("#feed_mail").val();
		var phone = $("#feed_phone").val();
		var name = $("#feed_name").val();
		var sbj = $("#feed_sbj").val();

		if(msg=="")
		{
			$("#feed_msg_err").html("*Please fill this field.");
			contact_form.feed_msg.focus();
			return false;
		}
		else
		{
			$("#feed_msg_err").html("");
		}
		var nm_pat=/^[a-zA-Z ]+$/;
		if(name=="")
		{
			$("#feed_name_err").html("*Please enter the Name.");
			contact_form.feed_name.focus();
			return false;
		}
		else if(!nm_pat.test(name))
        {
            $('#feed_name_err').html("*Please enter valid Name.");
            contact_form.feed_name.focus();
            return false;          
        }
		else
		{
			$("#feed_name_err").html("");
		}		

		var mail_pat = /^([\w-\.]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([\w-]+\.)+))([a-zA-Z]{2,4}|[0-9]{1,3})(\]?)$/;
        if(email=="")
        {
            $('#feed_mail_err').html("*Please enter Email Address.");   
            contact_form.feed_mail.focus();
            return false;    
        }
        else if(!mail_pat.test(email))
        {
            $('#feed_mail_err').html("*Please enter proper Email Address.");
            contact_form.feed_mail.focus();
            //alert('role');
            return false;    
        }
        if(mail_pat.test(email))
        {
            $('#feed_mail_err').html("");
        }


        var phone_pat= /^\d{10}$/;
        if(phone=="")
        {
            $('#feed_phone_err').html("*Please enter Phone No.");
            contact_form.feed_phone.focus();
            return false;       
        }
        else if(!phone_pat.test(phone))
        {
            $('#feed_phone_err').html("*Please enter valid Phone No.");
            contact_form.feed_phone.focus();
            return false;          
        }
        else
        {
            $('#feed_phone_err').html("");
        }        

        if(sbj=="")
		{
			$("#feed_sbj_err").html("*Please fill this field.");
			contact_form.feed_sbj.focus();
			return false;
		}
		else
		{
			$("#feed_sbj_err").html("");
		}

	});
});