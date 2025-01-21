const popup = document.getElementById("popup");
const closeButton = document.querySelector(".close-button");
const showPopupButton = document.getElementById("student-btn");
const popupContent = document.querySelector(".popup-content");
console.log("showPopupButton:", showPopupButton);



showPopupButton.addEventListener("click", showSubscriptionPopup);
closeButton.addEventListener("click", hidePopup);






function showPopup(message) {
  document.getElementById("popup-message").textContent = message;
  popup.style.display = "block";
}

function hidePopup() {
  popup.style.display = "none";
}


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




function showSubscriptionPopup() {
    console.log("showPopupButton clicked");
  popupContent.innerHTML = `
            <span class="close-button">&times;</span>
            <form id="subscribe-form">
                <input type="text" id="promo" name="promo" placeholder="Endet your promocode" required>
                <button type="submit">Submit</button>
            </form>
        `;
  popup.style.display = "block";

  document
    .querySelector(".close-button")
    .addEventListener("click", function () {
      popup.style.display = "none";
    });

  const subscribeForm = document.getElementById("subscribe-form");
  subscribeForm.addEventListener("submit", function (event) {
    event.preventDefault(); // Prevent default form submission

    const promo = document.getElementById("promo").value;

    fetch("api/v1/subs", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ promo: promo }),
    })
      .then((response) => response.json())
      .then((data) => {
        console.log("Success:", data);
        popup.style.display = "none";
      })
      .catch((error) => {
        console.error("Error:", error);
      });
  });
}