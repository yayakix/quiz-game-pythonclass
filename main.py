from question_model import Question
from data import question_data

question_bank = []
for x in question_data:
    q_text = x['text']
    q_answ = x['answer']

    new_quest = Question(q_text, q_answ)
    question_bank.append(new_quest)

print(question_bank)