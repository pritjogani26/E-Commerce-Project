window.onload = function() {
    let today = new Date();
    let maxDate = new Date();
    today.setDate(today.getDate() + 2); // Set minimum check-in date to today + 2 days
    maxDate.setMonth(maxDate.getMonth() + 1); // Set maximum check-in and check-out date to 1 month from today

    let formattedCurrentDate = formatDate(today); // Format the current date
    let formattedMaxDate = formatDate(maxDate); // Format the maximum date

    document.getElementById("checkIn").setAttribute("min", formattedCurrentDate);
    document.getElementById("checkIn").setAttribute("max", formattedMaxDate);
    document.getElementById("checkOut").setAttribute("min", formattedCurrentDate);
    document.getElementById("checkOut").setAttribute("max", formattedMaxDate);
};

// Function to format the date to 'YYYY-MM-DDTHH:MM' format
function formatDate(date) {
    let year = date.getFullYear();
    let month = String(date.getMonth() + 1).padStart(2, '0');
    let day = String(date.getDate()).padStart(2, '0');
    let hours = String(date.getHours()).padStart(2, '0');
    let minutes = String(date.getMinutes()).padStart(2, '0');
    return `${year}-${month}-${day}T${hours}:${minutes}`;
}

function calculateTotalGuests() {
    const maleGuests = parseInt(document.getElementById('maleGuests').value);
    const femaleGuests = parseInt(document.getElementById('femaleGuests').value);
    const childrenGuests = parseInt(document.getElementById('childrenGuests').value);
    const rooms = parseInt(document.getElementById('rooms').value);

    const totalGuests = maleGuests + femaleGuests + childrenGuests;
    if (totalGuests == 0) {
        alert("Total Number of Guests must be more than 0.");
        return false;
    }
    if (rooms > totalGuests) {
        alert("Total rooms cannot be more than the total number of guests.");
        return false;
    }

    alert(`Total Guests: ${totalGuests} and Total Room you Selected : ${rooms}`);
    return true;
}

// Wait for the DOM to fully load before executing JavaScript
document.addEventListener("DOMContentLoaded", function() {
    const bookingForm = document.getElementById("bookingForm");
    const checkInInput = document.getElementById("checkIn");
    const checkOutInput = document.getElementById("checkOut");
    const roomsInput = document.getElementById("rooms");
    const submitButton = document.getElementById("submit");

    // Set the minimum check-in date to today + 2 days and maximum to 1 month from today
    const today = new Date();
    const minDate = new Date(today);
    minDate.setDate(minDate.getDate() + 2); // Minimum check-in date is today + 2 days
    const maxDate = new Date(today);
    maxDate.setMonth(maxDate.getMonth() + 1); // Maximum check-in and check-out date is 1 month from today

    // Format dates for HTML input attributes (YYYY-MM-DDTHH:MM format)
    const formattedMinDate = formatDate(minDate);
    const formattedMaxDate = formatDate(maxDate);

    // Set attributes for check-in and check-out inputs
    checkInInput.setAttribute("min", formattedMinDate);
    checkInInput.setAttribute("max", formattedMaxDate);
    checkOutInput.setAttribute("min", formattedMinDate);
    checkOutInput.setAttribute("max", formattedMaxDate);

    // Event listener for roomsInput change
    roomsInput.addEventListener('change', calculateAmount);

    // Event listener for checkInInput and checkOutInput change
    checkInInput.addEventListener('change', validateDates);
    checkOutInput.addEventListener('change', validateDates);

    // Event listener for form submission
    // bookingForm.addEventListener("submit", function(event) {
    //     event.preventDefault(); // Prevent form submission

    //     if (validateDates() && calculateTotalGuests()) {
    //         bookingForm.submit(); // Submit the form if all validations pass
    //     }
    // });

    // Function to validate check-in and check-out dates
    function validateDates() {
        const checkInDate = new Date(checkInInput.value);
        const checkOutDate = new Date(checkOutInput.value);

        // Check if check-out date is before check-in date
        if (checkOutDate < checkInDate) {
            alert("Please select a check-out date that is after the check-in date.");
            checkOutInput.value = "";
            return false;
        }

        // Check if the gap between check-in and check-out date is at least one day
        const oneDay = 24 * 60 * 60 * 1000; // One day in milliseconds
        const diffDays = Math.round((checkOutDate - checkInDate) / oneDay);
        if (diffDays < 1) {
            alert("The gap between check-in and check-out date should be at least one day.");
            checkOutInput.value = "";
            return false;
        }

        return true; // Dates are valid
    }

    // Function to calculate the total number of guests and validate against room selection
    function calculateTotalGuests() {
        const maleGuests = parseInt(document.getElementById('maleGuests').value) || 0;
        const femaleGuests = parseInt(document.getElementById('femaleGuests').value) || 0;
        const childrenGuests = parseInt(document.getElementById('childrenGuests').value) || 0;
        const rooms = parseInt(document.getElementById('rooms').value) || 0;

        const totalGuests = maleGuests + femaleGuests + childrenGuests;

        if (totalGuests === 0) {
            alert("Total number of guests must be more than 0.");
            return false;
        }

        if (rooms > totalGuests) {
            alert("Total rooms selected cannot be more than the total number of guests.");
            return false;
        }

        return true; // Total guests and rooms are valid
    }

    // Function to calculate the booking amount based on selected dates and rooms
    function calculateAmount() {
        const checkInDate = new Date(checkInInput.value);
        const checkOutDate = new Date(checkOutInput.value);

        if (checkOutDate < checkInDate) {
            document.getElementById('cost').value = 0; // Reset cost to 0 if dates are invalid
            return;
        }

        const oneDay = 24 * 60 * 60 * 1000; // One day in milliseconds
        const diffDays = Math.round((checkOutDate - checkInDate) / oneDay);
        const rooms = parseInt(document.getElementById('rooms').value) || 0;

        const amount = diffDays * rooms * 500; // Assuming 500 units of currency per room per day
        document.getElementById('cost').value = amount;
    }

    // Function to format date to 'YYYY-MM-DDTHH:MM' format for HTML input
    function formatDate(date) {
        const year = date.getFullYear();
        const month = String(date.getMonth() + 1).padStart(2, '0');
        const day = String(date.getDate()).padStart(2, '0');
        const hours = String(date.getHours()).padStart(2, '0');
        const minutes = String(date.getMinutes()).padStart(2, '0');
        return `${year}-${month}-${day}T${hours}:${minutes}`;
    }

    // Reset fields when the Reset button is clicked
    const resetButton = document.getElementById("reset");
    resetButton.addEventListener("click", function() {
        checkInInput.value = "";
        checkOutInput.value = "";
        document.getElementById('cost').value = ""; // Reset cost field
    });
});