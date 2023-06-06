import data
from PyQt6.QtWidgets import (
    QApplication, 
    QMainWindow, 
    QPushButton, 
    QLabel, 
    QVBoxLayout, 
    QWidget, 
    QTextEdit
)
from PyQt6.QtCore import QSize


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('My App')

        self.setFixedSize(QSize(900, 550))
        self.setMaximumSize(QSize(900, 400))

        self.label = QLabel()

        self.input = QTextEdit()
        self.input.setFixedSize(QSize(883, 200))

        button_1 = QPushButton('Encode')
        button_2 = QPushButton('Decode')
        button_3 = QPushButton('Copy')
        button_4 = QPushButton('Paste')

        button_1.clicked.connect(self.encode)
        button_2.clicked.connect(self.decode)
        button_3.clicked.connect(self.copy)
        button_4.clicked.connect(self.paste)

        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.label)
        layout.addWidget(button_1)
        layout.addWidget(button_2)
        layout.addWidget(button_3)
        layout.addWidget(button_4)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)
    
    def encode(self):
        text = self.input.toPlainText()
        self.label.setText(data.encode(text))
    
    def decode(self):
        text = self.input.toPlainText()
        self.label.setText(data.decode(text))

    def copy(self):
        c = QApplication.clipboard()
        if c != None:
            c.setText(self.label.text())

    def paste(self):
        c = QApplication.clipboard()
        self.input.setPlainText(c.text())



if __name__ == "__main__":
    app = QApplication([])

    window = MainWindow()
    window.show()

    app.exec()
