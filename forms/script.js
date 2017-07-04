function setup() {
  // Make the button call setResult function when clicked.
  $('#showMe').on("click", setResult);
}

function setResult() {
  // Get the values from text input and put it in span.
  var textValue = $('#userText').val();
  $('#userInput').text(textValue);
}

$(document).ready(setup);
