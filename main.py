from PyQt6.QtWidgets import QMainWindow, QTextEdit, QLineEdit, QPushButton, \
     QApplication
import sys


class ChatbotWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Chat GPT")

        self.setMinimumSize(600, 500)

        # Add chat aria widget
        self.chat_area = QTextEdit(self)
        self.chat_area.setGeometry(10, 10, 580, 390)
        self.chat_area.setReadOnly(True)

        # Add the input field widget
        self.input_field = QLineEdit(self)
        self.input_field.setGeometry(10, 410, 580, 30)

        # Add the button
        self.button = QPushButton("Send", self)
        self.button.setGeometry(500, 450, 87, 40)

        self.show()


app = QApplication(sys.argv)
main_window = ChatbotWindow()
sys.exit(app.exec())
