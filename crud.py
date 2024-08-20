from sqlalchemy.orm import Session
from .models import Question, Choice
from .schemas import QuestionCreate
from sqlalchemy.orm import Session
from .models import Question as QuestionModel
from .schemas import QuestionCreate

def create_question(db: Session, question: QuestionCreate) -> QuestionModel:
    db_question = QuestionModel(
        text=question.text,
        correct_choice_id=question.correct_choice_id,
    )
    db.add(db_question)
    db.commit()
    db.refresh(db_question)  
    return db.query(QuestionModel).filter(QuestionModel.id > 0).all()

def get_all_questions(db: Session):
    return db.query(Question).all()

def get_question_with_choices(db: Session, question_id: int):
    return db.query(Question).filter(Question.id == question_id).first()

def get_choice(db: Session, choice_id: int):
    return db.query(Choice).filter(Choice.id == choice_id).first()
