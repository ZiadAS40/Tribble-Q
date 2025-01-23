
let questions = [];

const quizContainer = document.getElementById("quiz-container");

const quizId = quizContainer.getAttribute("data-quiz-id");
const userId = quizContainer.getAttribute("data-user-id");
let timeLeft = parseInt(quizContainer.getAttribute("data-time"), 10) * 60;
const totalQuizTime = timeLeft;


fetch(`/api/v1/quiz/${quizId}`)
  .then((response) => response.json())
  .then((data) => {
    questions = data.questions;
    currentQuestionIndex = 0;
    const progressPercentage = ((totalQuizTime - timeLeft) / totalQuizTime) * 100;
    progressBar.style.width = progressPercentage + "%";
    startTimer();
    renderQuestion();
  })
  .catch((error) => {
    alert("Failed to load quiz. Please try again later.");
  });
console.log("timeLeft", timeLeft);
const progressBar = document.getElementById("progress-bar");

function startTimer() {
    console.log("timeLeft", timeLeft);
    const timerInterval = setInterval(() => {
        console.log("timeLeft", timeLeft);
        if (timeLeft <= 0) {
      clearInterval(timerInterval);
      submitQuiz();
    } else {
      timeLeft--;
      const progressPercentage = ((totalQuizTime - timeLeft) / totalQuizTime) * 100;
      progressBar.style.width = progressPercentage + "%";
    }
  }, 1000);
}


let currentQuestionIndex = 0;
const userAnswers = {};

function renderQuestion() {
  const question = questions[currentQuestionIndex];
  document.getElementById("question-title").innerText = question.tittle;
  const answersContainer = document.getElementById("answers-container");
  answersContainer.innerHTML = "";
  question.answers.forEach((answer, index) => {
    const answerElement = document.createElement("div");
    answerElement.classList.add("answer");
    answerElement.innerHTML = `
            <label>
                <input type="radio" name="answer" value="${answer}">
                ${answer}
            </label>
        `;
    answersContainer.appendChild(answerElement);
  });

  document.getElementById("next-button").innerText =
    currentQuestionIndex === questions.length - 1 ? "Submit" : "Next";

  document.querySelectorAll('.answers input[type="radio"]').forEach((radio) => {
    radio.addEventListener("change", function () {
      document.querySelectorAll(".answer").forEach((answer) => {
        answer.classList.remove("selected");
      });

      if (this.checked) {
        this.parentElement.parentElement.classList.add("selected");
      }
    });
  });
}
function nextQuestion() {
  const selectedAnswer = document.querySelector('input[name="answer"]:checked');
  if (!selectedAnswer) {
    showPopup("Please select an answer.");
    return;
  }

  userAnswers[questions[currentQuestionIndex]["id"]] = selectedAnswer.value;

  if (currentQuestionIndex === questions.length - 1) {
    submitQuiz();
  } else {
    currentQuestionIndex++;
    renderQuestion();
  }
}

function submitQuiz() {
    let score = 0;
    let length = 0;
  fetch(`/api/v1/quiz/${quizId}/submit`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      user_id: userId,
      answers: JSON.stringify(userAnswers),
    },
  }) .then((response) => {
    return response.json();
  })
  .then((data) => {
      score += parseInt(data.score, 10);
      length += parseInt(data.length, 10);
      const okButton = document.createElement("button");
      const popupContent = document.querySelector(".popup-content");
      
      okButton.innerText = "OK";
      okButton.style.marginTop = "20px";
      okButton.style.backgroundColor = "#4a90e2";
      okButton.addEventListener("click", () => {
      window.location.href = "/";
      });
      
      const tryAgainButton = document.createElement("button");
      tryAgainButton.innerText = "Try Again";
      tryAgainButton.style.marginTop = "20px";
      tryAgainButton.style.marginRight = "20px";
      tryAgainButton.style.backgroundColor = "red";
      
      if (score >= 0.7 * length) {
          showPopup(`You got it ${score} out of ${length}`, "success");
          tryAgainButton.style.display = "none";
      } else {
      
      
          tryAgainButton.addEventListener("click", () => {
              fetch(`/quiz/${quizId}?time=${totalQuizTime}`)
              .then((response) => {
                  if (response.status === 400) {
                      showPopup("Subscripe to get more tries", "error");
                      tryAgainButton.style.display = "none";
                  } else if (response.ok) {
                      window.location.href = `/quiz/${quizId}?time=${totalQuizTime}`;
                  } else {
                      showPopup("An unexpected error occurred.", "error");
                  }
              })
              .catch((error) => {
                  console.error("Error fetching the quiz:", error);
                  showPopup("An error occurred while trying to access the quiz.", "error");
                });
            });
            
            
            showPopup(`You got it ${score} out of ${length}`, "error");
        }
        
      popupContent.appendChild(tryAgainButton);
      popupContent.appendChild(okButton);
})
.catch((error) => {
    console.error(error);
    showPopup("An error occurred while trying to submit the quiz.", "error");
});

}
