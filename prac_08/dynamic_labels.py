"""
CP1404
Arpisitt Numsri
Convert miles to km program
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class NamesApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names_list = ["Nina", "Henry", "Lily", "Hina"]

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Widgets"
        self.root = Builder.load_file('dynamic_labels.kv')
        for name in self.names_list:
            temp_label = Label(text=name)
            self.root.ids.main.add_widget(temp_label)

        return self.root


NamesApp().run()
