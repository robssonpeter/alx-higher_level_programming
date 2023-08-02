$(document).ready(function () {
  // Function to fetch and display the translation
  function fetchTranslation () {
    const languageCode = $('#language_code').val(); // Get the entered language code

    // Make the API call to fetch the translation
    $.ajax({
      url: 'https://www.fourtonfish.com/hellosalut/hello/',
      data: { lang: languageCode }, // Pass the language code as a query parameter
      success: function (response) {
        // Update the text content of DIV#hello with the fetched translation
        $('#hello').text(response.hello);
      },
      error: function (error) {
        console.log(error);
        // Display an error message if the translation couldn't be fetched
        $('#hello').text('Error: Unable to fetch translation.');
      }
    });
  }

  // Attach a click event handler to the Translate button
  $('#btn_translate').on('click', function () {
    fetchTranslation(); // Call the function to fetch the translation
  });
});
