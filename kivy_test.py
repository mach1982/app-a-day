from kivy.app import App
#kivy.require("1.8.0")
from kivy.uix.label import Label


class SimpleKivyApp(App):
    def build(self):
        return Label()

if __name__ == "__main__":
    SimpleKivyApp().run()