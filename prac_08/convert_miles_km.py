"""
CP1404 Practical 08
Miles → Kilometres Converter
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM = 1.60934


class MilesConverterApp(App):
    km_output = StringProperty("0.0")

    def build(self):
        self.title = "Miles to Kilometres Converter"
        return Builder.load_file("convert_miles_km.kv")

    def handle_convert(self):
        miles = self.get_valid_miles()
        self.km_output = str(miles * MILES_TO_KM)

    def handle_increment(self, change):
        miles = self.get_valid_miles()
        miles += change
        self.root.ids.input_miles.text = str(miles)
        self.handle_convert()

    def get_valid_miles(self):
        try:
            return float(self.root.ids.input_miles.text)
        except ValueError:
            return 0.0


MilesConverterApp().run()
