$(document).on('click', 'DIV#toggle_header', () => {
  const current = $('header').attr('class');
  let replace;
  if (current === 'green') {
    replace = 'red';
  } else {
    replace = 'green';
  }
  $('header').removeClass(current);
  $('header').addClass(replace);
});
