document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('bookingForm');
    form.addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent the form from submitting normally

        // Here you can add your validation logic if needed
        // For demonstration purposes, we'll show the popup immediately
        showPopup();
    });

    function showPopup() {
        // Show the popup
        const popup = document.getElementById('successPopup');
        popup.style.display = 'block';

        // Optional: Close the popup after a few seconds (e.g., 3 seconds)
        setTimeout(function() {
            popup.style.display = 'none';
        }, 3000); // Adjust the timeout as needed
    }
});