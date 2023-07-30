"""
CP1404
Arpisitt Numsri
Convert miles to km program
"""


from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.properties import StringProperty


class NamesApp(App):
    def build(self):
        self.root = Builder.load_file('dynamic_labels.kv')
        names = ["Nina, Henry, Lily, Hina"]
        labels = BoxLayout(orientation='vertical')
        for name in names:
            label = Label(text=name)
            labels.add_widget(label)
        return labels


NamesApp().run