import sys
from operator import add, sub, mul, truediv
from PySide6.QtWidgets import QApplication, QMainWindow

from calculator_interface import Ui_MainWindow


class Calculator(QMainWindow):
    operators = {
        '+': add,
        '-': sub,
        '*': mul,
        '/': truediv,
    }

    def __init__(self):
        super(Calculator, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.enter_numbers()
        self.enter_operations()
        self.clear_methods()

    def enter_number(self, button_number: str):
        if self.ui.line_edit_entry.text() != '0':
            self.ui.line_edit_entry.setText(self.ui.line_edit_entry.text() + button_number)
        else:
            self.ui.line_edit_entry.setText(button_number)

    def enter_numbers(self):
        self.ui.button_1.clicked.connect(lambda: self.enter_number('1'))
        self.ui.button_2.clicked.connect(lambda: self.enter_number('2'))
        self.ui.button_3.clicked.connect(lambda: self.enter_number('3'))
        self.ui.button_4.clicked.connect(lambda: self.enter_number('4'))
        self.ui.button_5.clicked.connect(lambda: self.enter_number('5'))
        self.ui.button_6.clicked.connect(lambda: self.enter_number('6'))
        self.ui.button_7.clicked.connect(lambda: self.enter_number('7'))
        self.ui.button_8.clicked.connect(lambda: self.enter_number('8'))
        self.ui.button_9.clicked.connect(lambda: self.enter_number('9'))
        self.ui.button_0.clicked.connect(lambda: self.enter_number('0'))

    def clear_all(self):
        self.ui.line_edit_entry.setText('0')
        self.ui.label_temp.clear()

    def clear_entry(self):
        self.ui.line_edit_entry.setText('0')

    def backspace(self):
        number = self.ui.line_edit_entry.text()
        if len(number) > 1:
            self.ui.line_edit_entry.setText(number[:-1])
        else:
            self.ui.line_edit_entry.setText('0')

    def clear_methods(self):
        self.ui.button_clear.clicked.connect(self.clear_all)
        self.ui.button_ce.clicked.connect(self.clear_entry)
        self.ui.button_backspace.clicked.connect(self.backspace)

    def add_dot(self):
        if '.' not in self.ui.line_edit_entry.text():
            self.ui.line_edit_entry.setText(self.ui.line_edit_entry.text() + '.')

    def add_temp(self, math_symbol: str):
        if not self.ui.label_temp.text() or self.get_math_symbol() == '=':
            self.ui.label_temp.setText(self.remove_zeros(self.ui.line_edit_entry.text()) + math_symbol)
            self.ui.line_edit_entry.setText('0')

    def get_entry_number(self) -> int | float:
        if '.' in self.ui.line_edit_entry.text():
            return float(self.ui.line_edit_entry.text())
        return int(self.ui.line_edit_entry.text())

    def get_temp_number(self) -> int | float:
        if self.ui.label_temp.text():
            if '.' in self.ui.label_temp.text():
                return float(self.ui.label_temp.text()[:-1])
            return int(self.ui.label_temp.text()[:-1])

    def get_math_symbol(self):
        if self.ui.label_temp.text():
            return self.ui.label_temp.text()[-1]

    def negative_number(self):
        number = self.ui.line_edit_entry.text()
        if '-' not in number and number != '0':
            number = '-' + number
        else:
            number = number[1:]
        self.ui.line_edit_entry.setText(number)

    def get_square(self):
        number = self.ui.line_edit_entry.text()
        if '.' in number:
            number = float(number)
        else:
            number = int(number)

        self.ui.line_edit_entry.setText(str(number ** 2))

    def get_square_root(self):
        number = float(self.ui.line_edit_entry.text())
        self.ui.line_edit_entry.setText(str(number ** 0.5))

    def get_one_div_num(self):
        number = float(self.ui.line_edit_entry.text())
        self.ui.line_edit_entry.setText(str(1 / number))

    def get_interest(self):
        temp = float(self.ui.label_temp.text()[:-1])
        number = float(self.ui.line_edit_entry.text())
        self.ui.line_edit_entry.setText(str(temp / 100 * number))

    def enter_operations(self):
        self.ui.button_dot.clicked.connect(self.add_dot)
        self.ui.button_neg.clicked.connect(self.negative_number)
        self.ui.button_square.clicked.connect(self.get_square)
        self.ui.button_square_root.clicked.connect(self.get_square_root)
        self.ui.button_one_div_x.clicked.connect(self.get_one_div_num)
        self.ui.button_interest.clicked.connect(self.get_interest)
        self.ui.button_equal.clicked.connect(self.calculate)
        self.ui.button_mul.clicked.connect(lambda: self.add_temp('*'))
        self.ui.button_div.clicked.connect(lambda: self.add_temp('/'))
        self.ui.button_add.clicked.connect(lambda: self.add_temp('+'))
        self.ui.button_sub.clicked.connect(lambda: self.add_temp('-'))

    def calculate(self):
        entry = self.ui.line_edit_entry.text()
        temp = self.ui.label_temp.text()

        if temp:
            value = self.remove_zeros(
                str(self.operators[self.get_math_symbol()](self.get_temp_number(), self.get_entry_number())))
            self.ui.label_temp.setText(temp + self.remove_zeros(entry) + '=')
            self.ui.line_edit_entry.setText(value)

    @staticmethod
    def remove_zeros(number: str) -> str:
        num = float(number)
        if str(num)[-2:] == '.0':
            return str(int(num))
        return str(num)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec())
