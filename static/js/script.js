// Function to validate user input
function validateForm() {
    // Get the values of the input fields
    var message = $('#inputMessage').val();

    // Check if any of the fields are empty
    if (message.trim() === '') {
        alert('Please fill in the message.');
        return false; // Prevent form submission
    }

    // Check if the message input contains at least one sentence
    if (message.split('.').length <= 1) {
        alert('The Message field must contain at least one sentence ending with fullstop(.).');
        return false; // Prevent form submission
    }

    return true; // Allow form submission
}

// Attach the validateForm function to the form's onsubmit event
$(document).ready(function () {
    $('form[name="sentenceForm"]').submit(validateForm);
});
