function toggleDropdown(){
    const dropdown = document.getElementById("profiledropdown");
    
    if(dropdown.classList.contains("opacity-0")){
        dropdown.classList.remove("opacity-0","scale-95","pointer-events-none");
        dropdown.classList.add("opacity-100","scale-100");

    }
    else{
        dropdown.classList.remove("opacity-100","scale-100");
        dropdown.classList.add("opacity-0","scale-95","pointer-events-none");
    }
}

window.addEventListener('click',function(e){
    const button = document.getElementById('profilebtn');
    const dropdown = document.getElementById('profiledropdown');

    if(!button.contains(e.target) && !dropdown.contains(e.target) ){
        dropdown.classList.remove("opacity-100","scale-100");
        dropdown.classList.add("opacity-0","scale-95","pointer-events-none");
    }
});