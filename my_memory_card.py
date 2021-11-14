from PyQt5.QtCore import Qt
from PyQt5.Qtwidgets import (
    QAppiication, Qtwidget,
    QHBoxLayout, QVBoxLayout,
    QGroupBox, QButtonGroup, DRadioButton,
    QPushButton, QLabel ) 








app = QApplication([])

btn_OK = QPushButton('Ответить')
1b_Question = QLabel('Самый сложный вопрос в мире!')

RadioGroupBox = QGroupBox("Варианты ответов")

rbtn_1 = QRadioButton('Вариант 1')
rbtn_2 = QRadioButton('Вариант 2')
rbtn_3 = QRadioButton('Вариант 3')
rbtn_4 = QRadioButton('Вариант 4')

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

Layout_ans1 = QHBoxLayout()
Layout_ans2 = QVBoxLayout()
Layout_ans3 = QVBoxLayout()
Layout_ans2.addWidget(rbtn_1)
Layout_ans2.addWidget(rbtn_2)
Layout_ans3.addWidget(rbtn_3)
Layout_ans3.addWidget(rbtn_4)

Layout_ans1.addLayout(Layout_ans2)
Layout_ans1.addLayout(Layout_ans3)

RadioGroupBox.setLayout(Layout_ans1)

AnsGroupBox = QGroupBox("Результат теста")
1b_Result = QLabel('прав ты или нет?')
1b_Correct = QLabel('ответ будет тут!')
Layout_res = QVBoxLayout()
Layout_res.addWidget(1b_Result, aligment=(Qt.AlignLeft / Qt.AlignTop))
Layout_res.addWidget(1b_Correct, aligment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(Layout_res)

Layout_line1 = QHBoxLayout()
Layout_line2 = QHBoxLayout()
Layout_line3 = QHBoxLayout()

Layout_line1.addWidget(1b_Question, aligment=(Qt.AlignHCenter / Qt.AlignVCenter)
Layout_line2.addWidget(RadioGroupBox)
Layout_line2.addWidget(AnsGroupBox)
AnsGroupBox.hide()
