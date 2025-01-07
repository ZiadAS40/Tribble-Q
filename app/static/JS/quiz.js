
let questions = [
    {
        title: "Question 1: What is the capital of France?",
        answers: ["Paris", "London", "Berlin", "Madrid"]
    },
    {
        title: "Question 2: What is 2 + 2?",
        answers: ["3", "4", "5", "6"]
    },
    {
        title: "Question 3: What is the largest planet in our solar system?",
        answers: ["Earth", "Mars", "Jupiter", "Saturn"]
    }
];

// let user_id = null;
// let quiz_id = null;
// let q;

// console.log('quiz_id:', quiz_id);
// console.log('user_id:', user_id);
// console.log('questions:', questions);

// function glabalizer(q_id, u_id, qus) {
//     user_id = u_id;
//     quiz_id = q_id;
//     questions = qus;
//     q = q_id;
// }
// async function getQuiz(quiz_id, user_id) {
//     console.log('getQuiz called with:', quiz_id, user_id);
//     try {
//         const response = await fetch(`/api/v1/quiz/${quiz_id}`);
//         const data = await response.json();
//         location.href = "/quiz";
//         questions = data;
//         console.log('data:', questions);
//     } catch (error) {
//         console.error('Error fetching quiz:', error);
//     }
//     console.log('data:', questions);
// }

// (async () => {
//     await getQuiz(quiz_id, user_id);
//     console.log('q after', q);
// })();


// console.log('q after', q);

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
    console.log('renderQuestion called with:', questions);
    const question = questions[currentQuestionIndex];
    document.getElementById('question-title').innerText = question.title;
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

    userAnswers[questions[currentQuestionIndex + 1]["id"]] = selectedAnswer.value;

    if (currentQuestionIndex === questions.length - 1) {
        submitQuiz();
    } else {
        currentQuestionIndex++;
        renderQuestion();
    }
}

function submitQuiz() {
    const userId = user_id; // Replace with actual user ID
    fetch(`/api/vi/quiz/${quiz_id}/submit`, {
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
}

renderQuestion();


