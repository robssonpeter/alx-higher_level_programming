$(document).ready(function () {
  // Function to fetch and display the translation
  function fetchTranslation (languageCode) {
    const apiUrl = `https://www.fourtonfish.com/hellosalut/hello/${languageCode}`;

    // Perform the AJAX GET request to fetch the translation
    $.get(apiUrl, function (data) {
      // Display the translation in the HTML tag DIV#hello
      $('#hello').text(data.hello);
    });
  }

  // Event handler for the "Translate" button click
  $('#btn_translate').click(function () {
    const languageCode = $('#language_code').val();
    fetchTranslation(languageCode);
  });

  // Event handler for pressing "ENTER" when the focus is on INPUT#language_code
  $('#language_code').keypress(function (event) {
    if (event.which === 13) {
      const languageCode = $(this).val();
      fetchTranslation(languageCode);
    }
  });
});
