$(document).ready(function(){
    $('#sub_order').on("click",function(){

        var fname=$("#fnm").val();
        var nm_pat=/^[a-zA-Z ]+$/;
        if(fname=="")
        {
            $('#fnm_err').html("*Please enter Name.");
            checkoutform.fnm.focus();
            return false;       
        }
        else if(!nm_pat.test(fname))
        {
            $('#fnm_err').html("*Please enter valid Name.");
            checkoutform.fnm.focus();
            return false;          
        }
        else
        {
            $('#fnm_err').html("");
        }

        var lname=$("#lnm").val();
        if(lname=="")
        {
            $('#lnm_err').html("*Please enter Name.");
            checkoutform.lnm.focus();
            return false;       
        }
        else if(!nm_pat.test(lname))
        {
            $('#lnm_err').html("*Please enter valid Name.");
            checkoutform.lnm.focus();
            return false;          
        }
        else
        {
            $('#lnm_err').html("");
        }

        var cname=$("#cnm").val();
        var cnm_pat=/^[a-zA-Z. ]+$/;
        if(cname=="")
        {
            $('#cnm_err').html("*Please enter Company Name.");
            checkoutform.cnm.focus();
            return false;       
        }
        else if(!cnm_pat.test(cname))
        {
            $('#cnm_err').html("*Please enter valid Company Name.");
            checkoutform.cnm.focus();
            return false;          
        }
        else
        {
            $('#cnm_err').html("");
        }
        var cm=$("#cmail").val();
        var mail_pat = /^([\w-\.]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([\w-]+\.)+))([a-zA-Z]{2,4}|[0-9]{1,3})(\]?)$/;
        if(cm=="")
        {
            $('#cmail_err').html("*Please enter Email Address.");   
            checkoutform.cmail.focus();
            return false;    
        }
        else if(!mail_pat.test(cm))
        {
            $('#cmail_err').html("*Please enter proper Email Address.");
           checkoutform.cmail.focus();
            //alert('role');
            return false;    
        }
        if(mail_pat.test(cm))
        {
            $('#cmail_err').html("");
        }

        var cPhone=$('#cphone').val();
        var phone_pat= /^\d{10}$/;
        if(cPhone=="")
        {
            $('#cphone_err').html("*Please enter Phone No.");
            checkoutform.cphone.focus();
            return false;       
        }
        else if(!phone_pat.test(cPhone))
        {
            $('#cphone_err').html("*Please enter valid Phone No.");
            checkoutform.cphone.focus();
            return false;          
        }
        else
        {
            $('#cphone_err').html("");
        }        

        var cadd1 = $("#a1").val();
        if(cadd1=="")
        {
            $('#cadd_err').html("*Please enter address.");
            checkoutform.a1.focus();
            return false;          
        }
        else
        {
            $('#cadd_err').html("");
        }

        var town=$("#ct").val()
        if(town=="")
        {
            $('#ct_err').html("*Please enter City/Town.");
            checkoutform.ct.focus();
            return false;       
        }
        else if(!nm_pat.test(town))
        {
            $('#ct_err').html("*Please enter valid city name.");
            checkoutform.ct.focus();
            return false;          
        }
        else
        {
            $('#ct_err').html("");
        }

        var st=$("#state").val();
        if(st=="")
        {
            $('#st_err').html("*Please enter State.");
            checkoutform.state.focus();
            return false;       
        }
        else if(!nm_pat.test(st))
        {
            $('#st_err').html("*Please enter valid state Name.");
            checkoutform.state.focus();
            return false;          
        }
        else
        {
            $('#st_err').html("");
        }

        var post=$('#pc').val();
        var post_pat= /^\d{6}$/;
        if(post=="")
        {
            $('#pc_err').html("*Please enter Post Code.");
            checkoutform.pc.focus();
            return false;       
        }
        else if(!post_pat.test(post))
        {
            $('#pc_err').html("*Please enter valid Post Code.");
            checkoutform.pc.focus();
            return false;          
        }
        else
        {
            $('#pc_err').html("");
        }        
    });
});