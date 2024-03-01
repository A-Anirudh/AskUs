

// function darkModeToggle() {
//     var element = document.body;
//     element.classList.add("darkmode");
//     localStorage.setItem("mode", "dark");

// }


// function lightModeToggle() {
//     var element = document.body;
//     element.classList.remove("darkmode");
//     localStorage.setItem("mode", "light");


// }


// function toggleMode() {
//     let buttonText = document.getElementById("darkmode-button");
//     var element = document.body;
//     if (buttonText.innerHTML === 'Light mode') {
//         element.classList.add("darkmode");
//         document.getElementById("darkmode-button").innerHTML = 'Dark mode';
//         // document.getElementById("darkmode-button").onclick = darkModeToggle();
//     }
//     else {
//         element.classList.add("lightmode");
//         document.getElementById("darkmode-button").innerHTML = 'Light mode';
//         // document.getElementById("darkmode-button").onclick = lightModeToggle();

//     }
// }


window.onload = function () {
    setMode();
};

function setMode() {
    let mode = localStorage.getItem('mode');
    if (!mode) mode = 'light';
    let btn = document.getElementById("darkmode-button");


    // if (mode == 'darkmode') {
    //     btn.innerHTML = 'Light';
    // }
    // else {
    //     btn.innerHTML = 'Dark'
    // }


    document.body.classList.add(mode);
}


function toggleMode() {
    let element = document.body;
    let btn = document.getElementById("darkmode-button");
    let mode = localStorage.getItem('mode')

    if (!mode) mode = 'darkmode';

    if (mode == 'darkmode') {
        localStorage.setItem("mode", "light");
        element.classList.remove("darkmode");
        // btn.innerHTML = 'Dark';


    }
    else {
        localStorage.setItem("mode", "darkmode");
        element.classList.add("darkmode");
        // btn.innerHTML = 'Light';
        btn.style.size = '7px'
    }
}


function myFunction() {
    var element1 = document.getElementById("hint_id_username");
    if (element1) {
        element1.classList.remove("text-muted");
    }
    var element1 = document.getElementById("hint_id_password1");
    if (element1) {
        element1.classList.remove("text-muted");
    }
    var element1 = document.getElementById("hint_id_password2");
    if (element1) {
        element1.classList.remove("text-muted");
    }
    var element1 = document.getElementById("hint_id_username");
    if (element1) {
        element1.classList.remove("text-muted");
    }
    var element1 = document.getElementById("hint_id_username");
    if (element1) {
        element1.classList.remove("text-muted");
    }
    var element1 = document.getElementById("hint_id_username");
    if (element1) {
        element1.classList.remove("text-muted");
    }
}

myFunction()
