from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Generator
from .database import SessionLocal, engine
from .models import Base
from .schemas import QuestionCreate, Question, AnswerResponse
from .crud import (
    get_all_questions,
    get_choice,
)
from .models import Question as QuestionModel 

app = FastAPI()


Base.metadata.create_all(bind=engine)


def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/api/questions")
def create_question(question: QuestionCreate):
    return {"question": question}



@app.get("/api/questions", response_model=List[Question])
def list_questions_api(db: Session = Depends(get_db)):
    return get_all_questions(db)

@app.get("/api/question/{question_id}", response_model=Question)
def get_question_with_choices_api(question_id: int, db: Session = Depends(get_db)):
    question = db.query(QuestionModel).filter(QuestionModel.id == question_id).first()
    
    if not question:
        raise HTTPException(status_code=404, detail="Question not found")
    
    return question

def check_answer_api(
    question_id: int, choice_id: int, db: Session = Depends(get_db)
) -> AnswerResponse:
    question = get_question_with_choices_api(question_id, db)
    if not question:
        raise HTTPException(status_code=404, detail="Question not found")

    choice = get_choice(db, choice_id)
    if not choice:
        raise HTTPException(status_code=404, detail="Choice not found")

    is_correct = choice.id == question.correct_choice_id
    correct_answer = None
    if not is_correct:
        correct_answer = next(
            (c.text for c in question.choices if c.id == question.correct_choice_id),
            None,
        )

    return AnswerResponse(is_correct=is_correct, correct_answer=correct_answer)
