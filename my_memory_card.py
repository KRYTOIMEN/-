
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QRadioButton, QPushButton, QLabel, QButtonGroup)
from random import shuffle

class Question():
    ''' содержит вопрос, правильный ответ и три неправильных'''
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        # все строки надо задать при создании объекта, они запоминаются в свойства
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

questions_list = []
questions_list.append(Question('Государственный язык Бразилии', 'Португальский', 'Английский', 'Испанский', 'Бразильский'))
questions_list.append(Question('Какого цвета нет на флаге России?', 'Зелёный', 'Красный', 'Белый', 'Синий'))
questions_list.append(Question('Национальная хижина якутов', 'Ураса', 'Юрта', 'Иглу', 'Хата'))
questions_list.append(Question('Какой город называют "Городом невест"?', 'Иваново', 'Москва', 'Тамбов', 'Лондон'))
questions_list.append(Question('В каком году был основан Нижний Новгород?', '1221', '1000', '658', '1369'))
questions_list.append(Question('Кто несёт бревно?', 'Дедушка Ленин', 'Брежнев', ''))

app QApplication([])

window = QWidget()
window.setWindowTitle('Memo Card')
window.wove(100,100)
window.recize(300,300)

'''Интерфейс приложения'''
btn_OK = QPushButton('Ответить')
lb_Question = QLabel('В каком году основана Москва')

RadioGroupBox = QGroupBox('Варианты ответов')
rbtn_1 = QRadioButton('1147')
rbtn_2 = QRadioButton('1242')
rbtn_3 = QRadioButton('1861')
rbtn_4 = QRadioButton('1943')

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ans2.addwidget(rbtn_1)
layout_ans2.addwidget(rbtn_2)
layout_ans3.addwidget(rbtn_3)
layout_ans3.addwidget(rbtn_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLAyout(layout_ans1)

#Создание панели результата
AnsGroupBox = QGroupBox('Результаты теста')
lb_Rezult = QLabel('Прав ты или нет?')
lb_Correct = QLabel('Ответ будет тут!')

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)

#Размещение виджетов в окне
layout_line1 = QHBoxLayout()
lauout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_line1.addWidget(lb_Question, alignment = (Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addwidget(RadioGroupBox)

layout_line2.addWidget(AnsGroupBox)
RadioGroupBox.hide()

ayout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2) # кнопка должна быть большой
layout_line3.addStretch(1)

#Теперь разместим созданные строки друг под другом
layout_card = QVBoxLayout()
 
layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)

window.setLayout(layout_card)
 
'''Функция'''
def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')

def show_question():
        RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)

def test():
    if 'Ответить' == btn_OK.text():
        show_result()
    else:
        show_question()    

answer = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

def ask(q. Question):
    shuffle(answer)
    answer[0].setText(q.right_answer)
    answer[1].setText(q.wrong1)
    answer[2].setText(q.wrong2)
    answer[3].setText(q.wrong3)
    Ib_Question.setText(q.question)
    Ib_Correct.setText(q.right_answer)  
    show_question()

def show_correct(res):
    Ib_Result.setText(res)
    show_result()

def check_answer():
    if answer[0].isChecked():
        show_correct('Правильно!')
        window.score += 1
        print('Статистика\n-Всего вопросов: ', window.total, '\n-Правильных ответов: ', window.score)
        print('Рейтинг: ', (window.score/window.total*100), '%')
    else:
        if answer[1].isChecked() or answer[2].isChecked() or answer[3].isChecked():
            show_correct('Неверно!') 
            print('Рейтинг: ', (window.score/window.total*100), '%')

def next_question():
    window.total += 1
    print('Статистика\n-Всего вопросов: ', window.total, '\n правильных ответов: ', window.score)
    cur_question = randint(0, len(questions_list)-1)
    q = questions_list[window.cur_question]
    ask(q)

def click_OK():
    if btn_OK.text() == 'Ответить':
        check_answer()
    else:
        next_question()
           


ask('Государственный язык Бразилии', 'Португальский', 'Бразильский', 'Испанский', 'Итальянский')
btn_OK.clicked.connect(check_answer)
       
window.cur_question = -1

btn_OK.clicked.connect(click_OK)
next_question()

window.show()
app.exec()




































































































