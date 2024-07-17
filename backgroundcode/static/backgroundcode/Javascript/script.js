document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('bookingForm');

    form.addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent the form from submitting normally

        // Optional: Add validation logic if needed

        // Submit the form data via fetch or XMLHttpRequest
        fetch(form.action, {
            method: form.method,
            body: new FormData(form),
            headers: {
                'X-Requested-With': 'XMLHttpRequest', // Ensure this header is set for Django CSRF protection
            }
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                showPopup();
            } else {
                console.error('Booking was not successful.');
                // Optionally handle error cases or show error messages
            }
        })
        .catch(error => {
            console.error('Error submitting form:', error);
            // Handle any fetch errors or server errors
        });
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
