document.addEventListener('DOMContentLoaded', function() {
    // Logout functionality
    const logoutButton = document.getElementById('logoutButton');
    const confirmLogoutButton = document.getElementById('confirmLogoutButton');
    const logoutForm = document.getElementById('logoutForm');
    const logoutModal = $('#logoutModal');

    logoutButton.addEventListener('click', function() {
        // Show the modal
        logoutModal.modal('show');
    });

    confirmLogoutButton.addEventListener('click', function() {
        // Submit the form when the user confirms the logout
        logoutForm.submit();
    });

    // Booking form submission with success popup
    const bookingForm = document.getElementById('bookingForm');

    bookingForm.addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent the form from submitting normally

        // Here you can add your validation logic if needed
        // For demonstration purposes, we'll show the popup immediately
        showPopup();
    });

    function showPopup() {
        // Create the popup HTML content
        const popupHtml = `
            <div id="successPopup" class="popup">
                <h2>Success!</h2>
                <p>Your booking has been successfully submitted.</p>
            </div>
        `;

        // Append the popup to the body
        document.body.insertAdjacentHTML('beforeend', popupHtml);

        // Get the popup element
        const popup = document.getElementById('successPopup');

        // Show the popup
        popup.style.display = 'block';

        // Optional: Close the popup after a few seconds (e.g., 3 seconds)
        setTimeout(function() {
            popup.style.display = 'none';
            // Remove the popup from the DOM after it is hidden
            popup.remove();
        }, 3000); // Adjust the timeout as needed
    }
});
