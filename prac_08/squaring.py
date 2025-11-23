"""
CP1404 Practical 08
Modified Squaring Program
"""

from kivy.app import App
from kivy.lang import Builder


class SquareNumberApp(App):
    def build(self):
        self.title = "Square Number"
        return Builder.load_file("squaring.kv")

    def handle_square(self):
        try:
            value = float(self.root.ids.input_number.text)
        except ValueError:
            value = 0
        result = value ** 2
        self.root.ids.output_label.text = str(result)


SquareNumberApp().run()
