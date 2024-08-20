from pydantic import BaseModel
from typing import List, Optional

class ChoiceCreate(BaseModel):
    text: str

class QuestionCreate(BaseModel):
    text: str
    choices: List[ChoiceCreate]

class Choice(BaseModel):
    id: int
    text: str
    question_id: int

    class Config:
        orm_mode = True

class Question(BaseModel):
    id: int
    text: str
    choices: List[Choice] = []
    correct_choice_id: int

    class Config:
        orm_mode = True
        
        
class AnswerResponse(BaseModel):
    is_correct: bool
    correct_answer: Optional[str] = None
