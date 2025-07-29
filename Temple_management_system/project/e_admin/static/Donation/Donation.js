document.addEventListener("DOMContentLoaded", function() {
    // Add event listeners to radio buttons
    setDate();
    var radioButtons = document.querySelectorAll("input[type=radio][name='amount']");
    radioButtons.forEach(function(radio) {
        radio.addEventListener("change", function() {
            var amountTextBox = document.getElementById("amountc");
            if (this.value === "custom") {
                amountTextBox.readOnly = false;
                amountTextBox.value = ""; // Clear the text box
            } else {
                amountTextBox.readOnly = true;
                amountTextBox.value = this.value; // Set value from the selected radio button
            }
        });
    });
});

function setDate() {
    const currentDate = new Date().toISOString().split('T')[0];
    document.getElementById('today').value = currentDate;
}