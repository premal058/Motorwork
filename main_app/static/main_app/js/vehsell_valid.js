$(document).ready(function()
{
	$('#vehsell_form').on('submit', function() {
	
		
        
        var appdate = new Date(document.getElementById("veh_date").value);
        var date = new Date();
        var fdate = new Date();
        fdate.setDate(new Date().getDate()+8);
        if(appdate == 'Invalid Date')
        {
            $('#veh_date_err').html("*please enter date.");
            vehsell_form.veh_date.focus();
            return false;
        }
        else if(appdate < date)
        {
            $('#veh_date_err').html("*please enter date as specified above.");
            vehsell_form.veh_date.focus();
            return false;
        }
        else if(appdate > fdate)
        {
            $('#veh_date_err').html("*please enter date as specified above.");
            vehsell_form.veh_date.focus();
            return false;
        }
        else
        {
            $('#veh_date_err').html("");
        }

        //var txt;
        var r = confirm("after Clicked 'Ok' , mail will be sent to the seller that you booked the testslot, do you want to process??");
        if (r == true) {
            alert('Email has been sent to your registered Mail-ID')
        }
        else {
            return false;
        }
		        
	});
});