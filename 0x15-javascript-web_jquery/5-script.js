$(document).on('click', 'DIV#add_item', () => {
  $('UL.my_list').children().append('<li>Item</li>');
});
