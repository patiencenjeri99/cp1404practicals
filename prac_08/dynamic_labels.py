"""
CP1404 Practical 08
Dynamic Labels Example
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    def build(self):
        self.title = "Dynamic Labels"
        self.names = ["Patience", "Ruth", "Liam", "Shingi"]

        root = Builder.load_file("dynamic_labels.kv")
        main_box = root.ids.main

        for name in self.names:
            temp_label = Label(text=name)
            main_box.add_widget(temp_label)

        return root


DynamicLabelsApp().run()
