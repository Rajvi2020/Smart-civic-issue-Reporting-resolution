// Password Show / Hide

const togglePassword =
document.getElementById("togglePassword");


const password =
document.getElementById("password");



togglePassword.addEventListener(
"click",
function(){


    if(password.type === "password"){


        password.type="text";


        togglePassword.innerHTML =
        '<i class="fa-solid fa-eye-slash"></i>';


    }

    else{


        password.type="password";


        togglePassword.innerHTML =
        '<i class="fa-solid fa-eye"></i>';


    }


});




// Login Validation


const form =
document.querySelector("form");



form.addEventListener(
"submit",
function(event){


    const department =
    document.querySelector(
    'input[name="department_id"]'
    ).value.trim();



    const pass =
    document.querySelector(
    'input[name="password"]'
    ).value.trim();



    if(department==="" || pass===""){


        event.preventDefault();


        alert(
        "Please enter Department ID and Password"
        );


    }


});