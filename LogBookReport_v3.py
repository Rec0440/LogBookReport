from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QComboBox, QPushButton, QVBoxLayout
from PyQt5.QtGui import QIcon
from sys import exit, argv
from os import listdir, getcwd
from wrapper import Wrapper


# main class
class LogBookReport(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.file_name = ''                                                 # Excel-File name
        self.calc_year = ''                                                 # Period for calculate
        self.wr = None                                                      # controller referenced object
        self.list_xlsx = [f for f in listdir(getcwd()) if '.xlsx' in f]     # future excel-filename list
        self.default_comboBox1 = 0                                          # default value for file_name_comboBox

        self.setWindowTitle("LogBook")
        self.setWindowIcon(QIcon('titleicon.png'))
        self.setFixedSize(300, 180)
        self.lab1 = QLabel('Choose File name')
        self.filename_comboBox = QComboBox()
        self.set_values_fname_combo()
        self.filename_comboBox.setCurrentIndex(self.default_comboBox1)

        self.lab2 = QLabel('Choose period')
        self.period_comboBox = QComboBox()
        self.set_values_period_combo()

        self.calculate_btn = QPushButton("Calculate")
        self.calculate_btn.clicked.connect(self.on_clicked)

        self.box = QVBoxLayout()
        self.box.addWidget(self.lab1)
        self.box.addWidget(self.filename_comboBox)
        self.box.addWidget(self.lab2)
        self.box.addWidget(self.period_comboBox)
        self.box.addWidget(self.calculate_btn)
        self.setLayout(self.box)
        self.show()

    # handler button click
    def on_clicked(self):
        # capture parameters
        self.file_name = self.filename_comboBox.currentText()
        self.calc_year = self.period_comboBox.currentText()
        # create wrapper with current parameters
        self.wr = Wrapper(self.file_name, self.calc_year)
        self.wr.onclick_calculate()

    # set excel-file names list
    def set_values_fname_combo(self):
        for i, f in enumerate(self.list_xlsx):
            self.filename_comboBox.addItem(f, i)
            if f == 'PILOT_LOG_532.xlsx':
                self.default_comboBox1 = i

    # set period list
    def set_values_period_combo(self):
        for i in range(2019, 2029):
            self.period_comboBox.addItem(str(i))


if __name__ == '__main__':

    app = QApplication(argv)   # Qt main application
    LogBookReportApp = LogBookReport()
    exit(app.exec_())
