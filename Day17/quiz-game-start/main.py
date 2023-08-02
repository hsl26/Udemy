from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question['text']
    question_answer = question['answer']
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)
    
quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_qustion()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")

# number = 0
# score = 0
# for i in question_data:
#     number += 1
#     my_answer = input(f"Q.{number}: {i['text']} (True/False): ")
#     if my_answer.lower() == i['answer'].lower():
#         score += 1
#         print("You got it right!")
#         print(f"The correct answer was: {i['answer']}.")
#         print(f"Your current score is: {score}/{number}\n\n")
#     else:
#         print("That's wrong.")
#         print(f"The correct answer was: {i['answer']}.")
#         print(f"Your current score is: {score}/{number}\n\n")
    
