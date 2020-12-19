from PyQt5.QtWidgets import QPushButton


class Button(QPushButton):

    def __init__(self, text: str, *, width=640, height=480):
        super().__init__(text)
        self._text = text
        self.setGeometry(0, 0, width, height)
        self.setStyleSheet('font-size: 20px')

    @property
    def name(self):
        return self._text
