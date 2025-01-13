
let questions = [
    
];

const quizContainer = document.getElementById('quiz-container');

// Retrieve the quiz_id and user_id from the data attributes
const quizId = quizContainer.getAttribute('data-quiz-id');
const userId = quizContainer.getAttribute('data-user-id');


fetch(`/api/v1/quiz/${quizId}`)
    .then(response => response.json())
    .then(data => {
        questions = data; // Assuming the server returns an object with a 'questions' array
        currentQuestionIndex = 0; // Reset the question index
        console.log(questions);
        renderQuestion(); // Render the first question
    })
    .catch(error => {
        alert('Failed to load quiz. Please try again later.');
});

let timeLeft = 60;
const progressBar = document.getElementById('progress-bar');

function startTimer() {
const timerInterval = setInterval(() => {
    if (timeLeft <= 0) {
        clearInterval(timerInterval);
        submitQuiz();
    } else {
        timeLeft--;
        const progressPercentage = ((60 - timeLeft) / 60) * 100;
        progressBar.style.width = progressPercentage + '%';
    }
}, 1000);
}

startTimer();

let currentQuestionIndex = 0;
const userAnswers = {};


function renderQuestion() {
    console.log('renderQuestion called');
    const question = questions[currentQuestionIndex];
    document.getElementById('question-title').innerText = question.tittle;
    const answersContainer = document.getElementById('answers-container');
    answersContainer.innerHTML = '';
    question.answers.forEach((answer, index) => {
        const answerElement = document.createElement('div');
        answerElement.classList.add('answer');
        answerElement.innerHTML = `
            <label>
                <input type="radio" name="answer" value="${answer}">
                ${answer}
            </label>
        `;
        answersContainer.appendChild(answerElement);
    });

    document.getElementById('next-button').innerText = currentQuestionIndex === questions.length - 1 ? 'Submit' : 'Next';


    document.querySelectorAll('.answers input[type="radio"]').forEach((radio) => {
        radio.addEventListener('change', function() {

            document.querySelectorAll('.answer').forEach((answer) => {
                answer.classList.remove('selected');
            });

            if (this.checked) {
                this.parentElement.parentElement.classList.add('selected');
            }
        });
    });

}
function nextQuestion() {
    const selectedAnswer = document.querySelector('input[name="answer"]:checked');
    if (!selectedAnswer) {
        alert("Please select an answer.");
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
 // Replace with actual user ID
 console.log(userAnswers);
    fetch(`/api/v1/quiz/${quizId}/submit`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'user_id': userId,
            'answers': JSON.stringify(userAnswers)
        }
    }).then(response => {
        if (response.ok) {
            alert("Quiz submitted successfully!");
        } else {
            alert("Failed to submit quiz.");
        }
    });
    location.href = '/';
}


renderQuestion();
