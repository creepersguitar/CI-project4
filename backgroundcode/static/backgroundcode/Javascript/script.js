document.addEventListener("DOMContentLoaded", function() {
    var heroButton = document.querySelector(".hero-button");
    var bookingButton = document.querySelector(".booking-button");
    var profileForm = document.getElementById("profile-form");
    var heroText = document.querySelector(".hero-text");

    heroButton.addEventListener("click", function() {
        // Hide hero button and show profile form
        heroButton.classList.add("d-none");
        profileForm.classList.remove("d-none");
    });

    profileForm.addEventListener("submit", function(event) {
        event.preventDefault(); // Prevent form submission

        // Get form values
        var name = document.getElementById("inputName").value;
        var email = document.getElementById("inputEmail").value;
        var phone = document.getElementById("inputPhone").value;

        // Validate form (add your own validation logic as needed)
        if (name && email && phone) {
            // Simulate profile creation (you can replace this with actual logic)
            setTimeout(function() {
                // Update hero text and show booking button
                heroText.textContent = "Start Your Booking Process";
                profileForm.classList.add("d-none");
                bookingButton.classList.remove("d-none");
            }, 1000); // Simulate a delay for profile creation
        }
    });

    bookingButton.addEventListener("click", function() {
        heroText.textContent = "Now you can proceed with your booking!";
    });
});
