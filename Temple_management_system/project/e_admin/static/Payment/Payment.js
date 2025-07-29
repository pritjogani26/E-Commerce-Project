document.addEventListener("DOMContentLoaded", function() {
    const check1 = document.getElementById("check1");
    const check2 = document.getElementById("check2");
    const dacContainer = document.querySelector(".dac-container");
    const upiContainer = document.querySelector(".upi-container");
    const check01 = document.getElementById("check01");
    const check02 = document.getElementById("check02");
    // Initially, show dacContainer and hide upiContainer
    dacContainer.style.display = "block";
    upiContainer.style.display = "none";
    check01.style.backgroundColor = "black";

    // Event listener for check1
    check1.addEventListener("change", function() {
        if (this.checked) {
            check01.style.backgroundColor = "black";
            check02.style.backgroundColor = "green";
            dacContainer.style.display = "block";
            upiContainer.style.display = "none";
        }
    });

    // Event listener for check2
    check2.addEventListener("change", function() {
        if (this.checked) {
            check01.style.backgroundColor = "green";
            check02.style.backgroundColor = "black";
            dacContainer.style.display = "none";
            upiContainer.style.display = "block";
        }
    });

    // Trigger change event for check1 (since it's checked by default)
    check1.dispatchEvent(new Event("change"));
});