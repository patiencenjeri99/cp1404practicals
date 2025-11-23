"""
CP1404 Practical 08
Modified BoxLayout Demo starter file
"""

from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    def build(self):
        self.title = "Box Layout Demo"
        return Builder.load_file("box_layout.kv")


BoxLayoutDemo().run()
