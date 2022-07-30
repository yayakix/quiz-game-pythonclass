from main import question_bank


class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
    def next_question(self):
        self.question_number += 1
        print(self.question_list[self.question_number].text)
game_on = True
quizbrain = QuizBrain(question_bank)
while game_on:
    quizbrain.next_question()
    quizbrain.next_question()
    game_on = False
