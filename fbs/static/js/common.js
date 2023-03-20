// common js File


$(document).ready(function(){
    var response;
    $.validator.addMethod(
        "equalTo", 
        function(value, element,param) {
            return $(`${param}`).val()==value;
        },
        "Confirm Password should be equal to Password")
    
    $.validator.addMethod(
        "phone_no_check",
        function (value, element) {
            let regex = /^(0|\+91|91)?([2-9][0-9]{9})$/;
            return  value.trim() ?regex.test(value) : true ;
        },
        "Please enter mobile no in correct format"
        );
        
});