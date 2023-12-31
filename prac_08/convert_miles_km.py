"""
CP1404
Arpisitt Numsri
Convert miles to km program
"""

from kivy.app import App
from kivy.lang import Builder


MILES_TO_KM = 1.60934


class MilesApp(App):
    def build(self):
        """Constructor for Miles converter program"""
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self):
        """Validate input and convert to km"""
        value = self.get_validated_miles()
        result = value * MILES_TO_KM
        self.root.ids.output_label.text = str(result)

    def handle_increment(self, change):

        value = self.get_validated_miles() + change
        self.root.ids.input_text.text = str(value)
        self.handle_calculate()

    def get_validated_miles(self):
        """Checks if user input is a float, otherwise return error"""
        try:
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 0.0



MilesApp().run()
