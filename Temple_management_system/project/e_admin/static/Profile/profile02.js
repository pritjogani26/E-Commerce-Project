window.onload = function() {
    document.getElementById("dob").max = new Date(new Date().setFullYear(new Date().getFullYear() - 5)).toISOString().split("T")[0];
    const submitBtn = document.getElementById("submit");
    const makeChangesBtn = document.getElementById("change");
    const inputs = document.querySelectorAll('input, select');

    // Function to toggle form state
    function toggleFormState(readonly) {
        inputs.forEach(input => {
            input.readOnly = readonly;
        });
    }

    // Initial state
    toggleFormState(true); // Make all inputs readonly
    submitBtn.style.display = "none"; // Hide submit button
    makeChangesBtn.style.display = "block"; // Show make changes button

    // Event listener for make changes button
    makeChangesBtn.addEventListener("click", function() {
        toggleFormState(false); // Make inputs editable
        submitBtn.style.display = "block"; // Show submit button
        makeChangesBtn.style.display = "none"; // Hide make changes button
    });

    // Event listener for submit button
    submitBtn.addEventListener("click", function() {
        let mobileNo = document.getElementById("mobileno").value;
        let pincode = document.getElementById("pincode").value;

        // Mobile No validation
        if (mobileNo.length !== 10 || isNaN(mobileNo)) {
            alert("Mobile No must be a 10-digit number.");
            return;
        }

        // Pincode validation
        if (pincode.length !== 6 || isNaN(pincode)) {
            alert("Pincode must be a 6-digit number.");
            document.getElementById("pincode").value = "";
            return;
        }

        toggleFormState(true); // Make all inputs readonly
        submitBtn.style.display = "none"; // Hide submit button
        makeChangesBtn.style.display = "block"; // Show make changes button
    });

    // Form submission validation
    let bookingForm = document.getElementById("bookingForm");
    bookingForm.addEventListener("submit", function(event) {
        event.preventDefault();
        // Validation code removed from here
    });
};