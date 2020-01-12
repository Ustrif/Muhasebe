from PyQt5.QtWidgets import QPushButton,QVBoxLayout,F,QComboBox,qApp,QMainWindow,QLabel,QLineEdit,QWidget,QApplication,QHBoxLayout,QLayout,QFormLayout

class MyMainWindow(QMainWindow):
    def __init__(self, parent = None):
        super(MyMainWindow, self).__init__(parent)

        self.main_widget = QWidget(self)
        ...
        self.form_widget = FormWidget(self)
        #This is my UI widget

        self.main_layout = QVBoxLayout(self.main_widget)
        self.main_layout.sizeConstraint = QLayout.SetDefaultConstraint
        self.main_layout.addWidget(self.form_widget.main_widget)
        #form_widget has its own main_widget where I put all other widgets onto

        self.main_widget.setLayout(self.main_layout)
        self.setCentralWidget(self.main_widget)