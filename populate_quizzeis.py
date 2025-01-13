from app.routes import db, app
from app.models.quiz import Quiz
from app.models.question import Question
from app.models.user import User
import uuid



with app.app_context():
    # Create quizzes
    user = User.query.filter_by(username="ziad").first()
    quiz1 = Quiz(
        title="Basic English Grammar",
        instructions="Choose the correct answer for each question.",
        time=30,  # 30 minutes
        description="Test your knowledge of basic English grammar.",
        cate = "en",
        quiz_owner_id=user.id  # Replace with actual owner ID
    )

    # Add quizzes to the session
    print(quiz1.id)
    print(quiz1)
    db.session.add(quiz1)



    # Create questions for quiz1
    question1 = Question(
        id=str(uuid.uuid4()),
        question="What is the past tense of 'go'?",
        options="went,goed,goes,going",
        answer="went",
        number=1,
        category="Grammar",
        quiz_id=quiz1.id
    )

    question2 = Question(
        id=str(uuid.uuid4()),
        question="Which is a noun?",
        options="run,quickly,apple,blue",
        answer="apple",
        number=2,
        category="Grammar",
        quiz_id=quiz1.id
    )

    # Create questions for quiz2
    question3 = Question(
        id=str(uuid.uuid4()),
        question="Choose the correct word: She is very ____ at math.",
        options="good,well,badly,goodly",
        answer="good",
        number=1,
        category="Vocabulary",
        quiz_id=quiz1.id
    )

    question4 = Question(
        id=str(uuid.uuid4()),
        question="Choose the correct word: The cat is ____ the table.",
        options="on,at,in,over",
        answer="on",
        number=2,
        category="Vocabulary",
        quiz_id=quiz1.id
    )

    # Add questions to the session
    db.session.add(question1)
    db.session.add(question2)
    db.session.add(question3)
    db.session.add(question4)

    # Commit the session to save the quizzes and questions to the database
    db.session.commit()