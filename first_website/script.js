alert("Hello " + player_name);
player_guess = prompt("Guess Rock, Paper Or Scissors");
computer_guess = randomInteger(1, 3);
if (player_guess == computer_guess) {
  document.getElementById("user_feedback").innerHTML =
    "<em>You Guessed Correct 👍</em>";
} else {
  document.getElementById("user_feedback").innerHTML =
    "<em>Wrong 👎</em><p> You Chose " +
    player_guess +
    "!" +
    "<p> The Answer Was " +
    computer_guess +
    "!";
}

function randomInteger(min, max) {
  return Math.floor(Math.random() * (max - min + 1) + min);
}
