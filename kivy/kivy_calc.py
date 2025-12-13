from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.label import Label


class CalculatorLayout(BoxLayout):
    def calculate(self):
        try:
            num1 = float(self.ids.num1.text)
            num2 = float(self.ids.num2.text)
            operation = self.ids.operation_spinner.text

            if operation == 'Addition':
                result = num1 + num2
            elif operation == 'Subtraction':
                result = num1 - num2
            elif operation == 'Multiplication':
                result = num1 * num2
            elif operation == 'Division':
                if num2 != 0:
                    result = num1 / num2
                else:
                    self.show_error("Cannot divide by zero.")
                    return
            else:
                self.show_error("Invalid operation.")
                return

            self.ids.result_label.text = f"Result: {result}"

        except ValueError:
            self.show_error("Please enter valid numbers.")

    def show_error(self, message):
        popup = Popup(title='Error',
                      content=Label(text=message),
                      size_hint=(0.6, 0.4))
        popup.open()


class CalculatorApp(App):
    def build(self):
        return CalculatorLayout()


if __name__ == '__main__':
    CalculatorApp().run()
