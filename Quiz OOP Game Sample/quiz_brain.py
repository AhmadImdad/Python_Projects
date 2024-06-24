class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.questions = question_list
        self.score = 0
        self.answer=""

    def show_question(self):
        print(f"\nQ{self.question_number + 1}.{self.questions[self.question_number].text}? "
              f"(True/False) :")
        self.answer = input().lower()
        self.question_number += 1

    def check_answer(self):
        if (self.answer == self.questions[self.question_number - 1].answer.lower()
                or self.answer == self.questions[self.question_number - 1].answer[0].lower()):
            self.score += 1
            print("You got the right answer!!!")
            print(f"The correct answer is : {self.questions[self.question_number - 1].answer}.")
            print(f"Score : {self.score}/{self.question_number}.")
        else:
            print("Wrong answer !!!")
            print(f"The correct answer is : {self.questions[self.question_number - 1].answer}.")
            print(f"Your score is : {self.score}/{self.question_number}")

    def question_remain(self):
        if self.question_number < len(self.questions):
            return True
        else:
            return False
