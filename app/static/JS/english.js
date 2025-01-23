const popup = document.getElementById("popup");
const showPopupButton = document.getElementById("student-btn");
const popupContent = document.querySelector(".popup-content");

if (showPopupButton) {
  showPopupButton.addEventListener("click", showSubscriptionPopup);
}

function showPopup(message, type) {
  let fontAwesomeClass;

  if (type === "success") {
    fontAwesomeClass = "fas fa-check-circle";
  } else if (type === "error") {
    fontAwesomeClass = "fas fa-bug";
  } else {
    fontAwesomeClass = "fas fa-message";
  }

  popupContent.innerHTML = "";
  popupContent.innerHTML = `
        <span class="close-button">&times;</span>
        <i id="popup-icon" class="${fontAwesomeClass}"></i>
        <p id="popup-message">${message}</p>
        `;

  if (type === "success") {
    document.getElementById("popup-icon").style.color = "green";
  } else if (type === "error") {
    document.getElementById("popup-icon").style.color = "red";
  } else {
    document.getElementById("popup-icon").style.color = "#4a90e2";
  }

  popup.style.display = "block";
  document.querySelector(".close-button").addEventListener("click", () => {
    popup.style.display = "none";
  });
}

function handleQuizClick(url) {
  fetch(url)
    .then((response) => {
      if (response.status === 400) {
        showPopup("Subscripe to get more tries", "info");
      } else if (response.ok) {
        window.location.href = url;
      } else {
        showPopup("An unexpected error occurred.", "error");
      }
    })
    .catch((error) => {
      console.error("Error fetching the quiz:", error);
      showPopup("An error occurred while trying to access the quiz.", "error");
    });
}

function showSubscriptionPopup() {
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
    event.preventDefault();

    const promo = document.getElementById("promo").value;

    fetch("api/v1/subs", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ promo: promo }),
    })
      .then((response) => {
        if (response.ok) {
          popup.style.display = "none";
          showPopup("Subscription successful!", "success");
        } else {
          popup.style.display = "none";
          showPopup("Unvalid promocode", "error");
        }
      })
      .catch((error) => {
        console.error("Error:", error);
      });
  });
}
