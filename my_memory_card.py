#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QPushButton, QLabel, QRadioButton, QButtonGroup
from random import *
app = QApplication([])

window = QWidget()
window.setWindowTitle('Тест')



#Надо бы доделать игру


btn_OK = QPushButton('Ответить')
lb_Question = QLabel('Лучшая игра')
RadioGroupBox = QGroupBox('Варианты ответов')
rbnt_1 = QRadioButton('Кс')
rbnt_2 = QRadioButton('Бравл старс')
rbnt_3 = QRadioButton('Фортнайт')
rbnt_4 = QRadioButton('пабг')

layout_ans1 = QHBoxLayout()
layout_ans2 = QHBoxLayout()
layout_ans3 = QHBoxLayout()
layout_ans2.addWidget(rbnt_1)
layout_ans2.addWidget(rbnt_2)
layout_ans3.addWidget(rbnt_3)
layout_ans3.addWidget(rbnt_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)

AnsGroupBox = QGroupBox('Ваши результаты')
ans_result = QLabel('ты прав/не прав')
ans_correct = QLabel('правильный ответ:')
layout_res = QVBoxLayout()
layout_res.addWidget(ans_result, (Qt.AlignHCenter) | Qt.AlignVCenter)
layout_res.addWidget(ans_correct, (Qt.AlignHCenter) | Qt.AlignVCenter)
AnsGroupBox.setLayout(layout_res)

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()
class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
RadioGroup = QButtonGroup()
RadioGroup.addButton(rbnt_1)
RadioGroup.addButton(rbnt_2)
RadioGroup.addButton(rbnt_3)
RadioGroup.addButton(rbnt_4)

layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter) | Qt.AlignVCenter)
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
AnsGroupBox.hide()

layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2)
layout_line3.addStretch(1)

layout_card= QVBoxLayout()

layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)



question_list = []
question_list.append(Question('Что лучше вб или озон', 'Вб кормит пацыки', 'Озон поит вы чо', 'Я лучше на рынке вещи куплю', 'Ало какой вб я на алике закупаюсь'))
question_list.append(Question('Почему роберт помаз?', 'Так сказала сама мать природа', 'Потому что он ушел с алгоритмитики', 'Потому что Артем батон и Роберт помаз идеальное дуо', 'Для баланса вселенной'))
question_list.append(Question('Откуда мы с Амиром знакомы', 'В садике в одной группе были', 'В баре познакомились', 'С одной школы', 'Он мой троюродный брат по линии моего кота'))
window.setLayout(layout_card)

def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbnt_1.setChecked(False)
    rbnt_2.setChecked(False)
    rbnt_3.setChecked(False)
    rbnt_4.setChecked(False)
    RadioGroup.setExclusive(True)
def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')
answers = [rbnt_1, rbnt_2, rbnt_3, rbnt_4]
def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    ans_correct.setText(q.right_answer)
    show_question()
def show_correct(res):
    ans_result.setText(res)
    show_result()
def check_answer():
    if answers[0].isChecked():
        show_correct("Правильно!")
        window.score += 1
        print('Статистика\n-Всего вопросов:', window.total,'\n-Правильных ответов:', window.score)
        print('Рейтинг:', (window.score/window.total*100), '%')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неправильно!')
            print('Рейтинг:', (window.score/window.total*100), '%')
def next_question():
    window.total +=1
    print('Статистика\n-Всего вопросов:', window.total,'\n-Правильных ответов:', window.score)
    cur_question = randint(0, len(question_list)-1)
    q = question_list[cur_question]
    ask(q)
def click_OK():
    if btn_OK.text() == 'Ответить':
        check_answer()
    else:
        next_question()

window.score = 0
window.total = 0
window.cur_question = -1
btn_OK.clicked.connect(click_OK)
next_question()
window.show()
app.exec()