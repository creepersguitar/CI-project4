document.addEventListener("DOMContentLoaded", function() {
    // Get references to elements in the DOM
    var bookingForm = document.getElementById("booking-form");
    var heroText = document.querySelector(".hero-text");

    // Add event listener for booking form submission
    bookingForm.addEventListener("submit", function(event) {
        event.preventDefault(); // Prevent form submission

        // Get booking form values
        var bookingDate = document.getElementById("date").value.trim();
        var bookingTime = document.getElementById("time").value.trim();
        var numberOfGuests = document.getElementById("guests").value.trim();

        // Validate booking form fields
        if (!bookingDate) {
            alert("Please select a booking date.");
            return;
        }

        if (!bookingTime) {
            alert("Please select a booking time.");
            return;
        }

        if (!numberOfGuests || isNaN(numberOfGuests) || numberOfGuests <= 0) {
            alert("Please enter a valid number of guests.");
            return;
        }

        // Simulate booking creation (replace this with actual logic)
        setTimeout(function() {
            // Update hero text and reset form
            heroText.textContent = "Your booking is confirmed!";
            bookingForm.reset();
        }, 1000); // Simulate a delay for booking creation
    });
});