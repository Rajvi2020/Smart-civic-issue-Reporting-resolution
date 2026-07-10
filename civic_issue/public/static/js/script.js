// Navbar Shadow

window.addEventListener("scroll",function(){

    let nav=document.querySelector("nav");

    if(window.scrollY>50){

        nav.classList.add("shadow-2xl");

    }
    else{

        nav.classList.remove("shadow-2xl");

    }

});