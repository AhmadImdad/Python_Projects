import html


class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        check = self.still_has_questions()
        if check:
            self.current_question = self.question_list[self.question_number]
            self.question_number += 1
            self.current_question.text = html.unescape(self.current_question.text)
            return f"Q.{self.question_number}: {self.current_question.text}"
        else:
            return "Game End"

    def check_answer(self, user_answer):
        check = False
        if self.question_number != 10:
            check = self.still_has_questions()
        else:
            check = True
            self.question_number += 1
        if check:
            correct_answer = self.current_question.answer
            if user_answer.lower() == correct_answer.lower():
                self.score += 1
                return self.score
            else:
                return self.score
        else:
            return self.score
