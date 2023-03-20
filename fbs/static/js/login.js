
$("#login_form").validate({
    rules: {
    contact_info: {
        required: true,
      },
      password: {
        required: true,
      },
    },
    messages: {
        contact_info: {
            required: "Please enter your phone number.",
        },
        password:{
            required:"Please enter your password"
        }
    },
    errorClass: "errorClass", //apply a css class for error if you have style for valid
    validClass: "validClass", //apply a css class for error if you have style for error
  
    submitHandler: function (form) {
      form.submit();
    }
});
  