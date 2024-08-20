# Unfinished-qandafastapi23
This is an unfinished version of my fastapi project for a questions and answers app.

Following endpoints in mind:

Post api/questions – to create a question with choices and correct answer (add at least 3 choices) and we should have only one correct answer per question

Get api/questions - List all questions

Get api/question/{question_id} - List question with just all choices dont show correct on this api

Get api/question/{question_id}/{choice_id} - Response if answer is correct or not (if Wrong show correct answer , if correct answer just say awesome correct answer)
