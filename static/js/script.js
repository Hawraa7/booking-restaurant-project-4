// Function to confirm if the user really wants to cancel the booking
function confirmDelete(bookingId) {
    // Display a confirmation dialog to the user
    if (confirm("Are you sure you want to cancel this booking?")) {
        // If the user confirms, redirect them to the cancel URL for the given booking ID
        window.location.href = `/cancel/${bookingId}/`;
    }
}

// Function to filter bookings based on the selected year
function filterBookings() {
    // Get the selected year filter value from the dropdown menu
    let yearFilter = document.getElementById("filterYear").value;
    // Get the current year from the system
    let currentYear = new Date().getFullYear();
    // Get all the elements representing booking items in the list
    let bookings = document.querySelectorAll(".booking-item");

    // Loop through each booking item to apply the filtering logic
    bookings.forEach(booking => {
        // Extract the year from the 'data-year' attribute of each booking
        let bookingYear = parseInt(booking.getAttribute("data-year"));
        let matchesFilter = false;  // Flag to track if the current booking matches the filter

        // Check if the extracted year is a valid number
        if (!isNaN(bookingYear)) {
            // If the filter is set to 'all', show all bookings
            if (yearFilter === "all") {
                matchesFilter = true;
            } 
            // If the filter is 'last', show bookings from last year
            else if (yearFilter === "last" && bookingYear === currentYear - 1) {
                matchesFilter = true;
            } 
            // If the filter is 'current', show bookings from the current year
            else if (yearFilter === "current" && bookingYear === currentYear) {
                matchesFilter = true;
            } 
            // If the filter is 'next', show bookings for next year
            else if (yearFilter === "next" && bookingYear === currentYear + 1) {
                matchesFilter = true;
            }
        }

        // If the current booking matches the filter criteria, display it
        if (matchesFilter) {
            booking.style.setProperty('display', 'flex', 'important');
        } else {
            // Otherwise, hide the booking from view
            booking.style.setProperty('display', 'none', 'important');
        }
    });
}
