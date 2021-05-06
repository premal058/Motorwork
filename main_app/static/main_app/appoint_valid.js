$(document).ready(function()
{
	$('#app_sub').on("click",function()
	{
		var buy_year = $('#buy_year').val();

		var buy_year_pat= /^\d{4}$/;
		if(buy_year=="")
		{
			$('#buy_year_err').html("please enter Year.");
			appointment.buy_year.focus();
			return false;
		}
		else if(!buy_year_pat.test(buy_year))
		{
			$('#buy_year_err').html("please enter valid year.");
			appointment.buy_year.focus();
			return false;	
		}
		else if(buy_year> new Date().getFullYear())
		{
			$('#buy_year_err').html("please enter valid year.");
			appointment.buy_year.focus();
			return false;		
		}
		else 
		{
			$('#buy_year_err').html("");
		}

		var app_mil=$("#app_mlg").val();
		var app_mil_pat= /^\d{2}$/;
		if(app_mil=="")
		{
			$('#app_mlg_err').html("please enter Mileage.");
			appointment.app_mlg.focus();
			return false;
		}
		else if(!app_mil_pat.test(app_mil))
		{
			$('#app_mlg_err').html("please enter valid Mileage.");
			appointment.app_mlg.focus();
			return false;	
		}
		else 
		{
			$('#app_mlg_err').html("");
		}			

		var veh_num=$('#veh_no').val();
		var rto_num=/(([A-Za-z]){2,3}(|-)(?:[0-9]){1,2}(|-)(?:[A-Za-z]){2}(|-)([0-9]){1,4})|(([A-Za-z]){2,3}(|-)([0-9]){1,4})/;

		if(veh_num=="")
		{
			$('#veh_no_err').html("please enter RTO registered Number.");
			appointment.veh_no.focus();
			return false;
		}
		else if(!rto_num.test(veh_num))
		{
			$('#veh_no_err').html("please enter valid RTO registered Number.");
			appointment.veh_no.focus();
			return false;	
		}
		else 
		{
			$('#veh_no_err').html("");
		}	

		var app_Name=$("#app_name").val();
        var nm_pat=/^[a-zA-Z]+$/;
        if(app_Name=="")
        {
            $('#app_name_err').html("*Please enter Name.");
            appointment.app_name.focus();
            return false;       
        }
        else if(!nm_pat.test(app_Name))
        {
            $('#app_name_err').html("*Please enter valid Name.");
            appointment.app_name.focus();
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
            $('#app_mail_err').html("*Please enter Address.");
            appointment.app_mail.focus();
            return false;       
        }
        else if(!email_pat.test(app_Mail))
        {
            $('#app_mail_err').html("*Please enter valid Email Address.");
            appointment.app_mail.focus();
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
            appointment.app_phone.focus();
            return false;       
        }
        else if(!phone_pat.test(app_Phone))
        {
            $('#app_phone_err').html("*Please enter valid Phone No.");
            appointment.app_phone.focus();
            return false;          
        }
        else
        {
            $('#app_phone_err').html("");
        }


        var app_Add=$("#app_add").val();
        var add_pat=/^[0-9a-zA-Z,/ ]+$/;
        if(app_Add=="")
        {
            $('#app_add_err').html("*Please enter Address.");
            appointment.app_add.focus();
            return false;       
        }
        else if(!add_pat.test(app_Add))
        {
            $('#app_add_err').html("*Please enter valid Address.");
            registerForm.app_add.focus();
            return false;          
        }
        else
        {
            $('#app_add_err').html("");
        }        
	});
});