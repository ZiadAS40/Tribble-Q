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
        time=90,  # 90 minutes
        description="Challenge your vocabulary with advanced English words.",
        cate="en",
        quiz_owner_id=user.id  # Ensure this is the correct user ID
    )

    # Add the new quiz to the session
    db.session.add(quiz2)

    # Create questions for the new quiz
    questions = [
        Question(
            id=str(uuid.uuid4()),
            question="What is the synonym of 'abundant'?",
            options="scarce,plentiful,rare,limited",
            answer="plentiful",
            number=1,
            category="Vocabulary",
            quiz_id=quiz2.id
        ),
        Question(
            id=str(uuid.uuid4()),
            question="Choose the correct word: The scientist made a ____ discovery.",
            options="significant,insignificant,minor,unimportant",
            answer="significant",
            number=2,
            category="Vocabulary",
            quiz_id=quiz2.id
        ),
        Question(
            id=str(uuid.uuid4()),
            question="What is the antonym of 'diligent'?",
            options="lazy,hardworking,meticulous,careful",
            answer="lazy",
            number=3,
            category="Vocabulary",
            quiz_id=quiz2.id
        ),
        Question(
            id=str(uuid.uuid4()),
            question="Choose the correct word: The manager was ____ to the new proposal.",
            options="receptive,hostile,indifferent,unaware",
            answer="receptive",
            number=4,
            category="Vocabulary",
            quiz_id=quiz2.id
        ),
        Question(
            id=str(uuid.uuid4()),
            question="What is the synonym of 'meticulous'?",
            options="careless,thorough,sloppy,negligent",
            answer="thorough",
            number=5,
            category="Vocabulary",
            quiz_id=quiz2.id
        ),
        Question(
            id=str(uuid.uuid4()),
            question="Choose the correct word: The artist's work was ____ by critics.",
            options="acclaimed,ignored,criticized,overlooked",
            answer="acclaimed",
            number=6,
            category="Vocabulary",
            quiz_id=quiz2.id
        ),
        Question(
            id=str(uuid.uuid4()),
            question="What is the antonym of 'obscure'?",
            options="clear,hidden,ambiguous,vague",
            answer="clear",
            number=7,
            category="Vocabulary",
            quiz_id=quiz2.id
        ),
        Question(
            id=str(uuid.uuid4()),
            question="Choose the correct word: The politician's speech was ____ with promises.",
            options="laden,devoid,empty,scarce",
            answer="laden",
            number=8,
            category="Vocabulary",
            quiz_id=quiz2.id
        ),
        Question(
            id=str(uuid.uuid4()),
            question="What is the synonym of 'resilient'?",
            options="fragile,robust,weak,delicate",
            answer="robust",
            number=9,
            category="Vocabulary",
            quiz_id=quiz2.id
        ),
        Question(
            id=str(uuid.uuid4()),
            question="Choose the correct word: The ____ of the situation was not lost on anyone.",
            options="gravity,lightness,frivolity,insignificance",
            answer="gravity",
            number=10,
            category="Vocabulary",
            quiz_id=quiz2.id
        ),
        Question(
            id=str(uuid.uuid4()),
            question="What is the antonym of 'conspicuous'?",
            options="hidden,obvious,noticeable,apparent",
            answer="hidden",
            number=11,
            category="Vocabulary",
            quiz_id=quiz2.id
        ),
        Question(
            id=str(uuid.uuid4()),
            question="Choose the correct word: The ____ of the novel was unexpected.",
            options="climax,beginning,prologue,foreword",
            answer="climax",
            number=12,
            category="Vocabulary",
            quiz_id=quiz2.id
        ),
        Question(
            id=str(uuid.uuid4()),
            question="What is the synonym of 'elaborate'?",
            options="simple,complex,plain,unadorned",
            answer="complex",
            number=13,
            category="Vocabulary",
            quiz_id=quiz2.id
        ),
        Question(
            id=str(uuid.uuid4()),
            question="Choose the correct word: The ____ of the project was a success.",
            options="culmination,initiation,beginning,commencement",
            answer="culmination",
            number=14,
            category="Vocabulary",
            quiz_id=quiz2.id
        ),
        Question(
            id=str(uuid.uuid4()),
            question="What is the antonym of 'benevolent'?",
            options="malevolent,kind,compassionate,generous",
            answer="malevolent",
            number=15,
            category="Vocabulary",
            quiz_id=quiz2.id
        ),
        Question(
            id=str(uuid.uuid4()),
            question="Choose the correct word: The ____ of the evidence was undeniable.",
            options="validity,falsity,irrelevance,insignificance",
            answer="validity",
            number=16,
            category="Vocabulary",
            quiz_id=quiz2.id
        ),
        Question(
            id=str(uuid.uuid4()),
            question="What is the synonym of 'arduous'?",
            options="easy,difficult,simple,effortless",
            answer="difficult",
            number=17,
            category="Vocabulary",
            quiz_id=quiz2.id
        ),
        Question(
            id=str(uuid.uuid4()),
            question="Choose the correct word: The ____ of the situation required immediate action.",
            options="urgency,delay,postponement,procrastination",
            answer="urgency",
            number=18,
            category="Vocabulary",
            quiz_id=quiz2.id
        )
    ]

    # Add the new questions to the session
    for question in questions:
        db.session.add(question)

    # Commit the session to save the new quiz and questions to the database
    db.session.commit()