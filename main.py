from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty

class MyGridLayout(GridLayout):
    time_input = ObjectProperty(None)

    def on_submit(self):
        time_text = self.time_input.text
        print("Fascia oraria inserita:", time_text)

class MyApp(App):
    def build(self):
        return MyGridLayout()

if __name__ == "__main__":
    MyApp().run()
