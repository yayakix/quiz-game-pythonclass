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
print(quizbrain.question_list[0].text)
while game_on:
    user_answer = input('true or false')
    if user_answer == quizbrain.question_list[quizbrain.question_number].answer:
        quizbrain.next_question()
    else:
        game_on = False
