$(document).ready(function () {
  function addListItem () {
    const newItem = '<li>Item</li>';
    $('.my_list').append(newItem);
  }

  // Function to remove the last LI element from the list
  function removeListItem () {
    $('.my_list li:last-child').remove();
  }

  // Function to clear all LI elements from the list
  function clearList () {
    $('.my_list').empty();
  }

  // Event listeners for the click events
  $('#add_item').on('click', addListItem);
  $('#remove_item').on('click', removeListItem);
  $('#clear_list').on('click', clearList);
});
