document.addEventListener("DOMContentLoaded", function() {
    // Get references to elements in the DOM
    var heroButton = document.querySelector(".hero-button");
    var bookingButton = document.querySelector(".booking-button");
    var profileForm = document.getElementById("profile-form");
    var bookingForm = document.getElementById("booking-form");
    var heroText = document.querySelector(".hero-text");
    var profileCreatedModal = new bootstrap.Modal(document.getElementById('profileCreatedModal'));

    // Add event listener for the hero button click
    heroButton.addEventListener("click", function() {
        // Hide hero button and show profile form
        heroButton.classList.add("d-none");
        profileForm.classList.remove("d-none");
    });

    // Add event listener for profile form submission
    profileForm.addEventListener("submit", function(event) {
        event.preventDefault(); // Prevent form submission

        // Get form values
        var name = document.getElementById("inputName").value.trim();
        var email = document.getElementById("inputEmail").value.trim();
        var phone = document.getElementById("inputPhone").value.trim();

        // Validate form fields
        if (!validateName(name)) {
            alert("Please enter a valid name without numbers.");
            return;
        }

        if (!validateEmail(email)) {
            alert("Please enter a valid email address.");
            return;
        }

        if (!validatePhone(phone)) {
            alert("Please enter a valid phone number.");
            return;
        }

        // Simulate profile creation (replace this with actual logic)
        setTimeout(function() {
            // Update hero text and show booking button
            heroText.textContent = "Start Your Booking Process";
            profileForm.classList.add("d-none");
            bookingButton.classList.remove("d-none");
            profileCreatedModal.show(); // Show profile created modal
        }, 1000); // Simulate a delay for profile creation
    });

    // Add event listener for the booking button click
    bookingButton.addEventListener("click", function() {
        // Hide booking button and show booking form
        bookingButton.classList.add("d-none");
        bookingForm.classList.remove("d-none");
        heroText.textContent = "Please fill in your booking details!";
    });

    // Add event listener for booking form submission
    bookingForm.addEventListener("submit", function(event) {
        event.preventDefault(); // Prevent form submission

        // Get booking form values
        var bookingDate = document.getElementById("inputBookingDate").value.trim();
        var bookingTime = document.getElementById("inputBookingTime").value.trim();
        var numberOfGuests = document.getElementById("inputGuests").value.trim();

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
            // Update hero text and reset forms
            heroText.textContent = "Your booking is confirmed!";
            bookingForm.classList.add("d-none");
            heroButton.classList.remove("d-none");
            profileForm.reset();
            bookingForm.reset();
        }, 1000); // Simulate a delay for booking creation
    });

    // Modal event listener to reset the form and button states
    document.getElementById('profileCreatedModal').addEventListener('hidden.bs.modal', function () {
        profileForm.reset();
        heroButton.classList.remove('d-none');
        bookingButton.classList.add('d-none');
        heroText.textContent = "Welcome to bite bait!";
    });

    // Helper function to validate name
    function validateName(name) {
        return name && !/\d/.test(name);
    }

    // Helper function to validate email
    function validateEmail(email) {
        var re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return re.test(email);
    }

    // Helper function to validate phone
    function validatePhone(phone) {
        var re = /^\d{10,15}$/; // Adjust the regex based on your phone number format
        return re.test(phone);
    }
});