$("#user_register").validate({
    rules: {
        firstName: {
        required: true,
      },
      lastName: {
        required: true,
      },
      mobile: {
        required: true,
        minlength:10,
        phone_no_check:true
      },
      password: {
        required: true,
      },
      confirmPassword: {
        required: true,
        equalTo: "#password",
      },
      gender:{
        required: true,
      },
      address:{
        required: true,
      },
      city:{
        required: true,
      },
      state:{
        required: true,
      },
      is_farmer:{
        required: true,
      },
      
    },
    messages: {
        is_farmer:{
          required: "Please Choose User type",
        },
        gender:{
          required: "Please Choose Anyone",
        },
        
    },
    errorClass: "errorClass", //apply a css class for error if you have style for valid
    validClass: "validClass", //apply a css class for error if you have style for error
    
    submitHandler: function (form) {
          form.submit();
    },
  });
  