$(document).ready(() => {
  $.ajax({
    type: 'GET',
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    success: (data) => {
      console.log(data);
      for (let x = 0; x < data.results.length; x++) {
        if (x === 0) {
          $('UL#list_movies').html('<li>' + data.results[x].title + '</li>');
        } else {
          $('UL#list_movies').children().append('<li>' + data.results[x].title + '</li>');
        }
      }
    }
  });
});
