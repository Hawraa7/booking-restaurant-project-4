function confirmDelete(bookingId) {
    if (confirm("Are you sure you want to cancel this booking?")) {
        window.location.href = `/cancel/${bookingId}/`;
    }
}

function filterBookings() {
    let yearFilter = document.getElementById("filterYear").value;
    let currentYear = new Date().getFullYear();
    let bookings = document.querySelectorAll(".booking-item");

    bookings.forEach(booking => {
        let bookingYear = parseInt(booking.getAttribute("data-year"));
        let matchesFilter = false;
        if (!isNaN(bookingYear)) {
            if (yearFilter === "all") {
                matchesFilter = true;
            } else if (yearFilter === "last" && bookingYear === currentYear - 1) {
                matchesFilter = true;
            } else if (yearFilter === "current" && bookingYear === currentYear) {
                matchesFilter = true;
            } else if (yearFilter === "next" && bookingYear === currentYear + 1) {
                matchesFilter = true;
            }
        }
        if (matchesFilter){
            booking.style.setProperty('display', 'flex', 'important');
        } else {
            booking.style.setProperty('display', 'none', 'important');
        }
    });
}