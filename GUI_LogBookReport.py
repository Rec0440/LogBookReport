from PyQt5 import QtWidgets
import sys
from os import listdir, getcwd


def on_clicked():
    print("File name:", filename_comboBox.currentText(), end=' - ')
    print("Period:", period_comboBox.currentText())


app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("LogBook")
window.resize(300, 150)
lab1 = QtWidgets.QLabel('Choose File name')

filename_comboBox = QtWidgets.QComboBox()
list_xlsx = [f for f in listdir(getcwd()) if '.xlsx' in f]
for i, f in enumerate(list_xlsx):
    filename_comboBox.addItem(f, i)
    if f == 'PILOT_LOG_532.xlsx':
        mycurrentindex = i
filename_comboBox.setCurrentIndex(mycurrentindex)

lab2 = QtWidgets.QLabel('Choose period')
period_comboBox = QtWidgets.QComboBox()
for i in range(2019, 2025):
    period_comboBox.addItem(str(i))
button = QtWidgets.QPushButton("Calculate")
button.clicked.connect(on_clicked)

box = QtWidgets.QVBoxLayout()
box.addWidget(lab1)
box.addWidget(filename_comboBox)
box.addWidget(lab2)
box.addWidget(period_comboBox)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec_())
