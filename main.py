from fastapi import FastAPI, HttpException, Depends
from pydantic import BaseModel
from typing import List

app = FastAPI()


class ChoiceBase(BaseModel):
    choice_text: str
    isCorrect: bool


class QuestionBase(BaseModel):
    question_text: str
    choices: List[ChoiceBase]
