from PyQt5.QtWidgets import QWidget, QLineEdit
from calculator.widgets.button import Button


class Calculator(QWidget):

    def __init__(self, *, init_x=100, init_y=150, width=500, height=600, title='Calculator'):
        super().__init__()
        self.setGeometry(0, 0, width, height)
        self.move(init_x, init_y)
        self.setWindowTitle(title)

        self._width = width
        self._height = height

        self._display: QLineEdit = None
        self._math_expression = ''

    def add_display(self, display: QLineEdit, height: int) -> None:
        self._display = display
        display.setParent(self)
        display.setGeometry(0, 0, self._width, height)

    def add_button(self, button: QWidget, shift_x: int, shift_y: int) -> None:
        button.setParent(self)
        button.move(shift_x, shift_y)

    def click(self, button: Button):
        print(f'Clicked on {button.name}')
        sep = ''
        try:
            int(button.name)
        except ValueError:
            sep = ' '

        if button.name == '=':
            self._calculate()
        else:
            self._math_expression = f'{self._math_expression}{sep}{button.name}'

        self._display.setText(self._math_expression)

    def _calculate(self):
        self._math_expression = str(eval(self._math_expression))
