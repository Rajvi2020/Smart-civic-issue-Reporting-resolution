// Password Show / Hide

const togglePassword = document.getElementById("togglePassword");

const password = document.getElementById("password");


if(togglePassword){

    togglePassword.addEventListener("click", function(){


        if(password.type === "password"){


            password.type = "text";


            togglePassword.innerHTML =
            '<i class="fa-solid fa-eye-slash"></i>';


        }
        else{


            password.type = "password";


            togglePassword.innerHTML =
            '<i class="fa-solid fa-eye"></i>';


        }


    });

}





// Form Validation


const signupForm = document.querySelector("form");


if(signupForm){


signupForm.addEventListener("submit", function(e){


    let departmentName =
    document.querySelector(
    'input[name="department_name"]'
    ).value.trim();



    let email =
    document.querySelector(
    'input[name="email"]'
    ).value.trim();



    let departmentID =
    document.querySelector(
    'input[name="department_id"]'
    ).value.trim();



    let pass =
    document.querySelector(
    'input[name="password"]'
    ).value.trim();



    let confirmPass =
    document.querySelector(
    'input[name="confirm_password"]'
    ).value.trim();





    // Empty Check


    if(
        departmentName === "" ||
        email === "" ||
        departmentID === "" ||
        pass === "" ||
        confirmPass === ""
    ){

        e.preventDefault();


        alert(
        "Please fill all fields"
        );


        return;

    }





    // Password Length


    if(pass.length < 6){


        e.preventDefault();


        alert(
        "Password must contain minimum 6 characters"
        );


        return;


    }






    // Password Match


    if(pass !== confirmPass){


        e.preventDefault();


        alert(
        "Password and Confirm Password do not match"
        );


        return;


    }




});

}