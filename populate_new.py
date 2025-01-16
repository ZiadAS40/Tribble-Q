from app.routes import db, app
from app.models.quiz import Quiz
from app.models.question import Question
from app.models.user import User
import uuid

with app.app_context():
    # Fetch the user who will own the quiz
    user = User.query.filter_by(username="ziad").first()

    # Create a new quiz
    quiz2 = Quiz(
        title="Advanced English Vocabulary",
        instructions="Select the most appropriate word for each sentence.",
        time=45,  # 45 minutes
        description="Challenge your vocabulary with advanced English words.",
        cate="en",
        quiz_owner_id=user.id  # Ensure this is the correct user ID
    )

    # Add the new quiz to the session
    db.session.add(quiz2)

    # Create questions for the new quiz
    question5 = Question(
        id=str(uuid.uuid4()),
        question="What is the synonym of 'abundant'?",
        options="scarce,plentiful,rare,limited",
        answer="plentiful",
        number=1,
        category="Vocabulary",
        quiz_id=quiz2.id
    )

    question6 = Question(
        id=str(uuid.uuid4()),
        question="Choose the correct word: The scientist made a ____ discovery.",
        options="significant,insignificant,minor,unimportant",
        answer="significant",
        number=2,
        category="Vocabulary",
        quiz_id=quiz2.id
    )

    # Add the new questions to the session
    db.session.add(question5)
    db.session.add(question6)

    # Commit the session to save the new quiz and questions to the database
    db.session.commit()