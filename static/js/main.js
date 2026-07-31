
// Navbar animation

window.addEventListener(
    "scroll",
    function(){
    
    
    const header=
    document.querySelector(".header");
    
    
    if(window.scrollY>50){
    
    header.style.boxShadow=
    "0 10px 30px rgba(0,0,0,.12)";
    
    }
    
    else{
    
    
    header.style.boxShadow=
    "0 5px 20px rgba(0,0,0,.08)";
    
    
    }
    
    
    });
    
    
    
    
    
    // Page loading animation
    
    document.addEventListener(
    "DOMContentLoaded",
    ()=>{
    
    
    document.body.style.opacity="1";
    
    
    });
    