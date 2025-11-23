"""
CP1404 Practical 08
Modified BoxLayout Demo with Greet and Clear functionality.
"""

from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    def build(self):
        self.title = "Box Layout Demo"
        return Builder.load_file("box_layout.kv")

    def handle_clear(self):
        name = self.root.ids.input_name.text
        self.root.ids.output_label.text = f"Hello, {name}"

    def handle_clear(self):
        self.root.ids.input_label.text = ""
        self.root.ids.output_label.text = ""

BoxLayoutDemo().run()
