window.onload = function() {
    document.getElementById("dob").max = new Date(new Date().setFullYear(new Date().getFullYear() - 5)).toISOString().split("T")[0];
    // document.getElementById("submit").addEventListener("click", validateForm);
};

// document.addEventListener("DOMContentLoaded", function() {
//     let bookingForm = document.getElementById("bookingForm");

//     bookingForm.addEventListener("submit", function(event) {
//         event.preventDefault();

//         let mobileNo = document.getElementById("mobileno").value;
//         let pincode = document.getElementById("pincode").value;
//         let password = document.getElementById("password").value;
//         let confirmPassword = document.getElementById("cpassword").value;
//         let loginButton = document.getElementsByClassName("login-button");
//         let profileButton = document.getElementsByClassName("profile-button");

//         // Mobile No validation
//         if (mobileNo.length !== 10 || isNaN(mobileNo)) {
//             alert("Mobile No must be a 10-digit number.");
//             return;
//         }

//         // Pincode validation
//         if (pincode.length !== 6 || isNaN(pincode)) {
//             alert("Pincode must be a 6-digit number.");
//             document.getElementById("pincode").value = "";
//             return;
//         }

//         if (password.length < 8) {
//             alert("Password must be at least 8 characters long.");
//             document.getElementById("password").value = "";
//             document.getElementById("cpassword").value = "";
//             return;
//         }

//         // Password validation
//         if (password !== confirmPassword) {
//             alert("Password and Confirm Password must match.");
//             document.getElementById("password").value = "";
//             document.getElementById("cpassword").value = "";
//             return;
//         }

//         // Form submission successful
//         alert("Form submitted successfully.");
//         // Redirect Path
//     });
// });