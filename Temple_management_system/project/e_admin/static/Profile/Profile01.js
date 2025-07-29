document.addEventListener("DOMContentLoaded", function() {
    // Default values
    const defaultValues = {
        fname: "prit",
        lname: "jogani",
        mobileno: "7490922474",
        emailid: "pritjogani2609@gmail.com",
        dob: "2003-09-26",
        state: "Gujarat",
        address: "112/5 Diamond Park Society, Uttamnagar, Nikol Gam Road.",
        area: "Nikol",
        city: "Ahmedabad",
        pincode: "382350"
    };

    // Loop through all input elements
    const inputs = document.querySelectorAll('input, select');
    inputs.forEach(input => {
        if (defaultValues[input.id]) {
            input.value = defaultValues[input.id];
        }
    });
});