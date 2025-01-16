var popup = document.getElementById("popup");
var closeButton = document.querySelector(".close-button");

function showPopup(message) {
  document.getElementById("popup-message").textContent = message;
  popup.style.display = "block";
}

function hidePopup() {
  popup.style.display = "none";
}

closeButton.addEventListener("click", hidePopup);

function handleQuizClick(url) {
  console.log("handleQuizClick called");
  console.log("url:", url);
  fetch(url)
    .then((response) => {
      if (response.status === 400) {
        showPopup("Subscripe to get more tries");
      } else if (response.ok) {
        window.location.href = url;
      } else {
        showPopup("An unexpected error occurred.");
      }
    })
    .catch((error) => {
      console.error("Error fetching the quiz:", error);
      showPopup("An error occurred while trying to access the quiz.");
    });
}
