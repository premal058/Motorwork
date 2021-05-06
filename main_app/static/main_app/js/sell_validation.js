$(document).ready(function(){

	$("#register-form").submit(function(){

		var veh_num= $('#first_name').val();
		var rc = $("#rc_book").val();
		var vpic = $("#vehicle_photo").val();
		
		var rto_num=/(([A-Za-z]){2,3}(|-)(?:[0-9]){1,2}(|-)(?:[A-Za-z]){2}(|-)([0-9]){1,4})|(([A-Za-z]){2,3}(|-)([0-9]){1,4})/;
		
		if(veh_num=="")
		{
			$('#sell_veh_no_err').html("*please enter RTO registered Number.");
			return false;
		}
		else if(!rto_num.test(veh_num))
		{
			$('#sell_veh_no_err').html("*please enter valid RTO registered Number.");
			return false;	
		}
		else 
		{
			$('#sell_veh_no_err').html("");
		}	

		var type = $("#veh_type").val();

		if(type=="")
		{
			$("#veh_type_err").html("*Please enter Type.");
			return false;
		}
		else if(type!="Gear" && type!="Gearless" && type!="gear" && type!="gearless")
		{
			$("#veh_type_err").html("*Please enter valid Type.");
			return false;	
		}
		else
		{
			$("#veh_type_err").html("");
		}

		var model= $("#model_no").val();
		var model_pat = /^[-*/ a-zA-Z0-9]+$/;
		if(model=="")
		{
			$("#model_no_err").html("Enter Model No.");
			return false;
		}
		else if(!model_pat.test(model))
		{
			$("#model_no_err").html("Enter valid Model No.");
			return false;	
		}
		else
		{
			$("#model_no_err").html(""); 	
		}

		var col = $("#veh_color").val();
		var col_pat= /^[ a-zA-Z]+$/;
		if(col=="")
		{
			$("#veh_col_err").html("*Enter the Proper Color");
			return false;
		}
		else if(!col_pat.test(col))
		{
			$("#veh_col_err").html("*Enter the Proper Color");
			return false;	
		}
		else
		{
			$("#veh_col_err").html("");
		}

		var comp = $("#Company").val();
		var comp_pat= /^[ ()a-zA-Z]+$/;
		if(comp=="")
		{
			$("#veh_comp_err").html("*Enter Company Name.");
			return false;
		}
		else if(!comp_pat.test(comp))
		{
			$("#veh_comp_err").html("*Enter  valid Company Name.");
			return false;	
		}
		else 
		{
			$("#veh_comp_err").html("");
		}


		var reg=$("#reg_year").val();
		if(reg=="")
		{
			$('#reg_year_err').html("please enter Registeration Date .");
			return false;
		}
		else 
		{
			$('#reg_year_err').html("");
		}

		var Mail=$("#sell_mail").val();
        var email_pat = /^([\w-\.]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([\w-]+\.)+))([a-zA-Z]{2,4}|[0-9]{1,3})(\]?)$/;
        if(Mail=="")
        {
            $('#sell_mail_err').html("*Please enter Email Address.");
            return false;       
        }
        else if(!email_pat.test(Mail))
        {
            $('#sell_mail_err').html("*Please enter valid Email Address.");
            return false;          
        }
        else
        {
            $('#sell_mail_err').html("");
        }

        var buy_year = $('#buy_year').val();

		var buy_year_pat= /^\d{4}$/;
		if(buy_year=="")
		{
			$('#buy_year_err').html("please enter Year.");
			return false;
		}
		else if(!buy_year_pat.test(buy_year))
		{
			$('#buy_year_err').html("please enter valid year.");
			return false;	
		}
		else if(buy_year> new Date().getFullYear())
		{
			$('#buy_year_err').html("please enter valid year.");
			return false;		
		}
		else 
		{
			$('#buy_year_err').html("");
		}

		var sell_Phone=$('#sell_phone').val();
        var phone_pat= /^\d{10}$/;
        if(sell_Phone=="")
        {
            $('#sell_phone_err').html("*Please enter Phone No.");
            return false;       
        }
        else if(!phone_pat.test(sell_Phone))
        {
            $('#sell_phone_err').html("*Please enter valid Phone No.");
            return false;          
        }
        else
        {
            $('#sell_phone_err').html("");
        }        

        var km= $("#veh_km").val();
        var km_pat=/^[,0-9]+$/;
        if(km=="")
        {
        	$("#veh_km_err").html("*Please Enter kilometers driven till date.");
        	return false;
        }
        else if(!km_pat.test(km))
        {
        	$("#veh_km_err").html("*Please Enter valid data into the field.");
        	return false;	
        }
        else
        {
        	$("#veh_km_err").html("");
        }

        var chasis = $("#veh_chasis").val();
        var chasis_pat = /^[A-Z0-9]+$/;
        if(chasis=="")
        {
        	$("#veh_chasis_err").html("*Enter Chasis Number of your vehicle.");
        	return false;
        }
        else if(chasis.length!=17)
        {
        	$("#veh_chasis_err").html("*Please enter Chasis Number in Proper valid format.");
        	return false;	
        }
        else if(chasis_pat.test(chasis))
        {
        	$("#veh_chasis_err").html("*Please enter Chasis Number in Proper valid format.");
        	return false;	
        }
        else
       	{
       		$("#veh_chasis_err").html("");
       	}

       	var price=$("#veh_price").val();
       	var price_pat= /[^0-9]/g;

       	if(price=="")
       	{
       		$("#veh_price_err").html("Enter price that you expect from your vehicle.");
       		return false;
       	} 
       	else if(price_pat.test(price))
       	{
       		$("#veh_price_err").html("Enter valid price .");
       		return false;	
       	}
       	else
       	{
       		$("#veh_price_err").html("");
       	}

		if(rc=="")
		{
			$("#rc_err").html('*please give vehicle RC book photo.');
			return false;
		}
		else
		{
			$("#rc_err").html('');
		}
		if(vpic=="")
		{
			$("#vpic_err").html('*please give vehicle photo.');
			return false;
		}
		else
		{
			$("#vpic_err").html('');
		}
	});
});