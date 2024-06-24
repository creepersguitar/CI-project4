document.addEventListener("DOMContentLoaded", function() {
    var heroButton = document.querySelector(".hero-button");
    var bookingButton = document.querySelector(".booking-button");
    var profileForm = document.getElementById("profile-form");
    var heroText = document.querySelector(".hero-text");
    var profileCreatedModal = new bootstrap.Modal(document.getElementById('profileCreatedModal'));

    heroButton.addEventListener("click", function() {
        // Hide hero button and show profile form
        heroButton.classList.add("d-none");
        profileForm.classList.remove("d-none");
    });

    profileForm.addEventListener("submit", function(event) {
        event.preventDefault(); // Prevent form submission

        // Get form values
        var name = document.getElementById("inputName").value.trim();
        var email = document.getElementById("inputEmail").value.trim();
        var phone = document.getElementById("inputPhone").value.trim();

        // Validate form
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

    bookingButton.addEventListener("click", function() {
        heroText.textContent = "Now you can proceed with your booking!";
    });

    // Helper functions for validation
    function validateName(name) {
        return name && !/\d/.test(name);
    }

    function validateEmail(email) {
        var re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return re.test(email);
    }

    function validatePhone(phone) {
        var re = /^\d{10,15}$/; // Adjust the regex based on your phone number format
        return re.test(phone);
    }
});
