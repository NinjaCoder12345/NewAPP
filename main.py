import kivy
from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget
from kivy.core.window import Window

#set the app size

Window.size = (500, 700)


class MyLayout(Widget):
    def clear(self):
        self.ids.calc_input.text = "0"
    def addNumber(self, number):
        prior = self.ids.calc_input.text
        if prior == "0" or prior == "0.0":
            self.ids.calc_input.text = ""
            self.ids.calc_input.text = number
        else:
            self.ids.calc_input.text = prior+number
    def equalToButton(self):
        prior = self.ids.calc_input.text
        self.ids.calc_input.text = str(float(eval(prior)))
    def signChanger(self):
        prior = self.ids.calc_input.text
        if "-" not in prior:
            self.ids.calc_input.text = f"-{prior}"
        else:
            self.ids.calc_input.text = self.ids.calc_input.text.replace("-", "")
    def correct(self):
        self.ids.calc_input.text = self.ids.calc_input.text[:-1]
class My(App):
    def build(self):
        return MyLayout()

if __name__ == "__main__":
    My().run()
