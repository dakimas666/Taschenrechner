import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QHBoxLayout, QVBoxLayout, QWidget, QLineEdit, QLabel
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon, QKeyEvent

class Taschenrechner(QMainWindow):
    def __init__(self):
        super().__init__()
        print("Initializing Taschenrechner application.")

        self.setWindowIcon(QIcon("graphics/calculator.png"))

        self.anzeige_rechenschritte = QLabel(self)
        self.anzeige_rechenschritte.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.anzeige_rechenschritte.setObjectName("anzeige_rechenschritte")
        self.anzeige_rechenschritte.setText("0")
        
        self.hauptanzeige = QLineEdit(self)
        self.hauptanzeige.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.hauptanzeige.setReadOnly(True)
        self.hauptanzeige.setText("0")

        self.button_list = [
            ["π", "(", ")", "DEL", "C"],
            ["x²", "7", "8", "9", "/"],
            ["√", "4", "5", "6", "*"],
            ["n!", "1", "2", "3", "-"],
            ["ln", "0", ".", "=", "+"]
        ]

        self.initUI()

    
    def initUI(self):        
        self.setWindowTitle("Taschenrechner")
        self.set_window_size()
        print("Window title and size set.")   
        print("Creating buttons.")

        vbox = QVBoxLayout()

        hbox_hauptanzeige = QHBoxLayout()
        hbox_hauptanzeige.addWidget(self.hauptanzeige)
        hbox_anzeige_rechenschritte = QHBoxLayout()
        hbox_anzeige_rechenschritte.addWidget(self.anzeige_rechenschritte)
        vbox.addLayout(hbox_anzeige_rechenschritte)
        vbox.addLayout(hbox_hauptanzeige)
        

        for ButtonRow in self.button_list:
            hbox = QHBoxLayout()
            for button in ButtonRow:
                print(f"Button: {button}")
                btn = QPushButton(button, self)
                btn.setObjectName(f"button_{button}")
                btn.clicked.connect(
                    lambda checked, value=button: self.button_clicked(value)
                )
                if button.isnumeric() or button == ".":
                    btn.setStyleSheet("background-color: lightgray;")

                hbox.addWidget(btn)

            vbox.addLayout(hbox)

        container = QWidget()
        container.setLayout(vbox)        
        self.setCentralWidget(container)
 
        self.setStyleSheet("""
                QPushButton {
                            font-size: 24px;
                            padding: 40px;
                            height: 70px;
                           }
                QLineEdit {
                            font-size: 50px;
                            padding: 10px;
                            height: 80px;
                            background-color: white;
                            color: blue;
                           }
                QLabel#anzeige_rechenschritte {
                            font-size: 24px;
                            height: 40px;
                            color: gray;
                            padding-right: 10px;
                            padding-top: 20px;
                            padding-bottom: 10px;
                           }
                           """)

    
    def set_window_size(self):
        print("Setting window size and centering the application.")
        app_width = 800
        app_height = 800
        available_geometry = QApplication.primaryScreen().availableGeometry()
        x = (available_geometry.width() - app_width) // 2
        y = (available_geometry.height() - app_height) // 2
        self.setGeometry(x, y, app_width, app_height)


    def keyPressEvent(self, event: QKeyEvent):
        key = event.key()
        print(f"Key pressed: {key}")
        match key:
            case Qt.Key.Key_0:
                self.button_clicked("0")
            case Qt.Key.Key_1:
                self.button_clicked("1")
            case Qt.Key.Key_2:
                self.button_clicked("2")
            case Qt.Key.Key_3:
                self.button_clicked("3")
            case Qt.Key.Key_4:
                self.button_clicked("4")
            case Qt.Key.Key_5:
                self.button_clicked("5")
            case Qt.Key.Key_6:
                self.button_clicked("6")
            case Qt.Key.Key_7:
                self.button_clicked("7")
            case Qt.Key.Key_8:
                self.button_clicked("8")
            case Qt.Key.Key_9:
                self.button_clicked("9")
            case Qt.Key.Key_Plus:
                self.button_clicked("+")
            case Qt.Key.Key_Minus:
                self.button_clicked("-")
            case Qt.Key.Key_Asterisk:
                self.button_clicked("*")
            case Qt.Key.Key_Slash:
                self.button_clicked("/")
            case Qt.Key.Key_Period:
                self.button_clicked(".")
            case Qt.Key.Key_Backspace | Qt.Key.Key_Delete:
                self.button_clicked("DEL")
            case Qt.Key.Key_ParenLeft:
                self.button_clicked("(")
            case Qt.Key.Key_ParenRight:
                self.button_clicked(")")
            case Qt.Key.Key_C:
                self.clear(clear_anzeige_rechenschritte=True, clear_hauptanzeige=True)
            case Qt.Key.Key_L:
                self.button_clicked("ln")
            case Qt.Key.Key_P:
                self.button_clicked("π")
            case Qt.Key.Key_S:
                self.button_clicked("√")
            case Qt.Key.Key_F:
                self.button_clicked("n!")
            case Qt.Key.Key_Equal | Qt.Key.Key_Return | Qt.Key.Key_Enter:
                self.button_clicked("=")
            case Qt.Key.Key_Escape:
                self.clear(clear_anzeige_rechenschritte=True, clear_hauptanzeige=True)    
            case _:
                print("Unhandled key.")

    
    def button_clicked(self, value):
        print(f"Button {value} clicked.")
        if value != "=":
            self.update_anzeigen(value)
        else:
            self.calculate_result()


    def update_anzeigen(self, text):
        if self.hauptanzeige.text() == "0":
            self.hauptanzeige.setText("")
        if self.anzeige_rechenschritte.text() == "0":
            self.anzeige_rechenschritte.setText("")

        print(f"Updating main display to: {text}")
        if text.isnumeric() or text == ".":            
            self.hauptanzeige.setText(self.hauptanzeige.text() + text)
        else:
            self.hauptanzeige.setText("")
        self.anzeige_rechenschritte.setText(self.anzeige_rechenschritte.text() + text)

    
    def calculate_result(self):
        print("Calculating result.")
        self.evaluate_parentheses(self.anzeige_rechenschritte.text())
        # Placeholder for actual calculation logic


    def evaluate_parentheses(self, expression):
        print("Evaluating parentheses in expression.")
        self.extract_parentheses2(self.anzeige_rechenschritte.text())
        return expression
    

    def extract_parentheses2(self, expression):
        print("Klammerausdrücke isolieren.")

        opening_indices = []
        closing_indices = []
        current_opening_index = 0
        current_closing_index = 0
        returned_expressions = []
        find_closing_parenthesis = False
        number_opening_parentheses = 0
        number_closing_parentheses = 0
        partial_expressions = []
        new_expression = ""

        for i, char in enumerate(expression):
            if not find_closing_parenthesis and char == '(':
                find_closing_parenthesis = True
                number_opening_parentheses += 1
                opening_indices.append(i)
                current_opening_index = i
            elif find_closing_parenthesis and char == '(':
                number_opening_parentheses += 1
            elif find_closing_parenthesis and char == ')' and number_opening_parentheses > number_closing_parentheses + 1:
                number_closing_parentheses += 1
            elif find_closing_parenthesis and char == ')' and number_opening_parentheses <= number_closing_parentheses + 1:
                closing_indices.append(i)
                current_closing_index = i
                start_parentheses = current_opening_index + 1
                stop_parentheses = current_closing_index
                returned_expressions.append(self.extract_parentheses2(expression=expression[start_parentheses : stop_parentheses])) 
        
        for i in range(len(opening_indices)):
            if i == 0:
                partial_expressions.append(expression[:opening_indices[i]])
            elif i > 0:
                partial_expressions.append(expression[closing_indices[i-1 : opening_indices[i]]])
        
        for i in range(len(partial_expressions)):
            if i < len(partial_expressions):
                new_expression += partial_expressions[i] + returned_expressions[i]
            else:
                new_expression += partial_expressions[i]

        new_expression = new_expression.replace("(", "")
        new_expression = new_expression.replace(")", "")
        print(f"new_expression: {new_expression}")
        
        return new_expression

        # expression = expression.replace("(", "")
        # expression = expression.replace(")", "")
        # print(f"Expression: {expression}")

        # return expression



    def extract_parentheses(self, expression):
        print("Parsing expression stack.")
        stack = []
        results = []
        for i, char in enumerate(expression):
            if char == "(":
                stack.append(i)
            elif char == ")":
                start = stack.pop()
                results.append(expression[start + 1:i])
        
        print(f"Extracted parentheses expressions: {results}")
        return results

    
    def clear(self, clear_anzeige_rechenschritte=False, clear_hauptanzeige=False):
        print("Clearing displays.")
        if clear_anzeige_rechenschritte:
            self.anzeige_rechenschritte.setText("0")
        if clear_hauptanzeige:
            self.hauptanzeige.setText("0")
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Taschenrechner()
    window.show()
    sys.exit(app.exec())

