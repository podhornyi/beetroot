import sys
from functools import partial

from PyQt5.QtWidgets import QApplication, QPushButton

from lesson_22_calculator.widgets.main import Calculator
from lesson_22_calculator.widgets.button import Button
from lesson_22_calculator.widgets.display import Display


buttons_data = {
    # row 1
    (0, 0): 'AC',
    (0, 1): '+/-',
    (0, 2): '%',
    (0, 3): '÷',
    # row 2
    (1, 0): '7',
    (1, 1): '8',
    (1, 2): '9',
    (1, 3): '*',
    # row 3
    (2, 0): '4',
    (2, 1): '5',
    (2, 2): '6',
    (2, 3): '-',
    # row 4
    (3, 0): '1',
    (3, 1): '2',
    (3, 2): '3',
    (3, 3): '+',
    # row 5
    (4, 0): '0',
    (4, 1): '1',
    (4, 2): ',',
    (4, 3): '='
}


def main():
    app = QApplication([])

    calculator = Calculator(init_x=700, init_y=250, width=400, height=600)
    calculator.add_display(Display(), 100)
    for row in range(5):
        for col in range(4):
            button_name = buttons_data[(row, col)]
            if row == 4 and col == 0:
                button = Button(button_name, width=200, height=100)
            elif row == 4 and col == 1:
                continue
            else:
                button = Button(button_name, width=100, height=100)

            clicker = partial(calculator.click, button=button)
            button.clicked.connect(clicker)
            calculator.add_button(
                button,
                shift_x=100 * col,
                shift_y=100 * row + 100
            )
    calculator.show()

    sys.exit(app.exec_())

