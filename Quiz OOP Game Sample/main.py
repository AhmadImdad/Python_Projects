from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank = list()
for i in range(len(question_data)):
    question_bank.append(Question(question_data[i]["text"],
                                  question_data[i]["answer"]))
quiz = QuizBrain(question_bank)
question_left = True
while question_left:
    quiz.show_question()
    quiz.check_answer()
    question_left = quiz.question_remain()
