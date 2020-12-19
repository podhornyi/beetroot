from PyQt5.QtWidgets import QLineEdit


class Display(QLineEdit):

    def __init__(self):
        super().__init__()
        self.setStyleSheet('font-size: 20px')
